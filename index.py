# Vai ser o início do scrapper dos ícones de ações e moedas
# Poder Mercado
# Time Rocket
# Moacir David
# Marizópolis > BSB
# Governo Poderal360

import requests
from bs4 import BeautifulSoup

url = 'https://br.tradingview.com/screener/'

print('[INFO] Iniciando requisição a página da Trading View...')

response = requests.get(url)

print('[INFO] Requisição concluída com status ' + response.status_code)

html_pagina = response.content

print('[INFO] Conteúdo da página passado para HTML')

print(html_pagina)