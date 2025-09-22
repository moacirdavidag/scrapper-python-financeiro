from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os
import requests
from urllib.parse import unquote, urlparse, parse_qs

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

print('[INFO] Iniciando requisição com Selenium à página de moedas...')
driver.get("https://www.sendwave.com/it/currency-converter/currencies")
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

cards = soup.find_all("div", {"data-testid": lambda x: x and x.startswith("cex-currency-card-")})

print(f"[INFO] Encontrados {len(cards)} cards de moedas")

os.makedirs("assets/icones/moedas", exist_ok=True)

for card in cards:
    code_tag = card.find("p", {"data-testid": "cex-currency-code"})
    name_tag = card.find("div", {"data-testid": "cex-currency-card-name"})
    img_tag = card.find("img", {"data-testid": lambda x: x and x.startswith("country-flag-")})
    
    codigo = code_tag.get_text(strip=True) if code_tag else None
    pais = name_tag.get_text(strip=True) if name_tag else None
    print("[INFO] Coletado: ", codigo, "-", pais)
    
    if img_tag and img_tag.get("src"):
        src = img_tag["src"]
        parsed = parse_qs(urlparse(src).query)
        if "url" in parsed:
            svg_path = unquote(parsed["url"][0])
            url_svg_real = "https://www.sendwave.com" + svg_path
            response = requests.get(url_svg_real)
            if response.status_code == 200:
                safe_name = f"{codigo}_{pais.replace(' ', '_')}"
                path = f"assets/icones/moedas/{safe_name}.svg"
                with open(path, "wb") as f:
                    f.write(response.content)
                print(f"[SUCCESS] Ícone salvo em {path}")
