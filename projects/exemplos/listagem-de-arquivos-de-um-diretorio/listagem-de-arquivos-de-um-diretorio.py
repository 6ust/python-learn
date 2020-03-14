import os

# Comando do prompt para listagem de arquivos dentro de uma Pasta / Diretório
# print(os.listdir("./pasta1/"))


limitColumn = 30
path = "./pasta1/"
x = os.listdir(path)

for file in x:
	print('_____________')
	print(file)
	readF = open(path + file, "r", encoding="utf8")
	for readL in readF:
		print(readL[:][:limitColumn])