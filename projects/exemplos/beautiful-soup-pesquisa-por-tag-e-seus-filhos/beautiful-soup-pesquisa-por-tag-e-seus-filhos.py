# pip install beautifulsoup4
# pip install urllib3

from bs4 import BeautifulSoup
import urllib.request

link_da_pagina = "https://www.kabum.com.br/produto/109717/adaptador-usb-md9-para-rj45-10-100mbps-8141?gclid=CjwKCAiAi_D_BRApEiwASslbJySaHE_pC-t7PeuJHpyW61UOcs_D3pu0Wsr_J4WJtTf9EWnGc8OH2xoCpMcQAvD_BwE"

# guardando o html da pagina
html = urllib.request.urlopen(link_da_pagina)

res = BeautifulSoup(html.read(), 'html.parser')

price = res.select("span.preco_desconto span span strong")

print("preço do produto --> " + str(price[0].get_text()))
