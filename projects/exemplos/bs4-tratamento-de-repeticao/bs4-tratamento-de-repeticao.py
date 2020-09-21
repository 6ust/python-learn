from bs4 import BeautifulSoup
import requests
import os

os.system("cls")
print("Aguarde...")
html = requests.get("https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2").content

soup = BeautifulSoup(html, 'html.parser')

# name = soup.find("span", class_="a-size-base-plus a-color-base a-text-normal")
name = soup.findAll("span", class_="a-size-base-plus")
pr = soup.findAll("span", class_="a-offscreen")

# for i in range(len(name)):
	# print(name[i] + str("\n"))
# print(soup.prettify())

j = len(name)
# print("2321")
# print(name)

if j == 0:
	# print("Não foram encontrados resultados tente novamente")
	os.system("py tst.py")
else:
	os.system("cls")
	for i in range(j):
		print(name[i])