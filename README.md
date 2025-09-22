# Mini-Projeto de Scraping de Ativos e Moedas

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.10.0-green.svg)](https://pypi.org/project/selenium/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12.2-orange.svg)](https://pypi.org/project/beautifulsoup4/)
[![Requests](https://img.shields.io/badge/Requests-2.31.0-red.svg)](https://pypi.org/project/requests/)

Este é um pequeno projeto de scraping em Python criado como apoio para outro projeto. O objetivo é coletar informações de **ações, commodities, índices e moedas**, juntamente com os **ícones correspondentes**, diretamente do **TradingView** e do site **Sendwave** (para moedas).

## Estrutura dos Scripts

* **acoes.py** – Coleta nomes, descrições e ícones das ações listadas no TradingView.
* **commodities.py** – Coleta nomes, descrições e ícones das commodities no TradingView.
* **indices.py** – Coleta nomes, descrições e ícones de índices/bolsas de valores no TradingView.
* **moedas.py** – Coleta códigos, nomes e bandeiras das moedas no site [Sendwave](https://www.sendwave.com/it/currency-converter/currencies).

## Pastas de saída

* `assets/icones/acoes/` – Ícones das ações
* `assets/icones/commodities/` – Ícones das commodities
* `assets/icones/indices/` – Ícones dos índices
* `assets/icones/moedas/` – Bandeiras das moedas

## Como rodar

1. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate    # Windows
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Certifique-se de ter o **ChromeDriver** compatível com sua versão do Chrome instalado e disponível no PATH.

4. Execute cada script individualmente:

```bash
python acoes.py
python commodities.py
python indices.py
python moedas.py
```

5. As imagens e informações coletadas serão salvas automaticamente nas pastas correspondentes dentro de `assets/icones/`.
