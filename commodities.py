from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os
import requests

def scrap_tradingview(url, pasta="commodities"):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    print(f'[INFO] Iniciando requisição com Selenium à página: {url}')
    driver.get(url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    tbody = soup.find("tbody", {"data-testid": "selectable-rows-table-body"})
    trs = tbody.find_all("tr") if tbody else []

    print(f"[INFO] Encontrados {len(trs)} TRs dentro do tbody alvo")

    os.makedirs(f"assets/icones/{pasta}", exist_ok=True)

    for tr in trs: 
        print('[INFO] Pegando célula do item')
        td = tr.find('td')
        if td:
            codigo_tag = td.find("a", class_="tickerNameBox-GrtoTeat")
            descricao_tag = td.find("sup", class_="tickerDescription-GrtoTeat")
            codigo = codigo_tag.get_text(strip=True) if codigo_tag else None
            descricao = descricao_tag.get_text(strip=True) if descricao_tag else None
            print("[SUCCESS] Coletado: ", codigo, "-", descricao)
            img_tag = td.find("img", class_="logo-PsAlMQQF")
            if img_tag and img_tag.get("src"):
                url_svg = img_tag["src"]
                response = requests.get(url_svg)
                if response.status_code == 200:
                    safe_name = codigo.replace("/", "_")
                    path = f"assets/icones/{pasta}/{safe_name}.svg"
                    with open(path, "wb") as f:
                        f.write(response.content)
                    print(f"[SUCCESS] Ícone salvo em {path}")
                else:
                    print(f"[ERRO] Não foi possível baixar {url_svg}")

    driver.quit()

scrap_tradingview("https://br.tradingview.com/markets/futures/quotes-metals/", "commodities")
