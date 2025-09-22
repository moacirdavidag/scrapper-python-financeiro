from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os
import requests

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

print('[INFO] Iniciando requisição com Selenium a página da TradeView...')
driver.get("https://br.tradingview.com/screener/")
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

tbody = soup.find("tbody", {"data-testid": "selectable-rows-table-body"})
trs = tbody.find_all("tr") if tbody else []

print(f"[INFO] Encontrados {len(trs)} TRs dentro do tbody alvo")

os.makedirs("assets/icones/acoes", exist_ok=True)

for tr in trs: 
    print('[INFO] Pegando célula da logo e o nome da ação')
    td = tr.find('td')
    if td:
        nome_acao_tag = td.find("a", class_="tickerNameBox-GrtoTeat")
        descricao_tag = td.find("sup", class_="tickerDescription-GrtoTeat")
        nome_acao = nome_acao_tag.get_text(strip=True) if nome_acao_tag else None
        descricao = descricao_tag.get_text(strip=True) if descricao_tag else None
        print("[SUCCESS] Coletado: ", nome_acao, "-", descricao)
        img_tag = td.find("img", class_="logo-PsAlMQQF")
        if img_tag and img_tag.get("src"):
            url_svg = img_tag["src"]
            response = requests.get(url_svg)
            if response.status_code == 200:
                path = f"assets/icones/acoes/{nome_acao}.svg"
                with open(path, "wb") as f:
                    f.write(response.content)
                print(f"[SUCCESS] Ícone salvo em {path}")
