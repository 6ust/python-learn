# Comandos do Sistema Operacional - OS 
import os
import sys
import shutil

# importação do RegEX
import re

pathRead  = "./pasta1/"
newFolder = "novo" 
pathSave  = "./" + newFolder + "/"


# Limite de Coluna estabelecido para salvamento/Atualização
limitColumn = 78


# Inicialização do Sistema
print("ATENÇÃO NÃO COLOQUE SEUS ARQUIVOS NA PASTA: [NOVO]")
print("POIS ELA SERA ATUALIZADA!")
print("Coloque seus arquivos na pasta: [pasta1].")
print("Pressione Enter, quando estiver pronto...")
x = input("Pronto?")

searchUser = str(input("O que gostaria de deletar do(s) Arquivo(s)"))

lenSearchUser = len(searchUser)


# exclui um diretório e todo o seu conteúdo.
shutil.rmtree(pathSave)

# Criar Diretorio
os.mkdir(pathSave)


fileDir = os.listdir(pathRead)
for file in fileDir:
	# print(fileDir)

	# Leitura de Documento/ Arquivo
	readFile = open(pathRead + file, "r", encoding="utf8")


	# Exibe o Nome do Arquivo
	print("------------------------------------")
	print(file)

	# Leitura por linhas do Documento
	# Salvamento de Documento/ Arquivo
	# print(pathSave + file)
	# saveFile = open(pathSave + file, "a", encoding="utf8")
	for readLineFile in readFile:
		x = re.search("arquivos",readLineFile)
		print("------------------------------------")
		if(not x):
			print(x)
			print(str(readLineFile) + "\n")
	print("------------------------------------")
	# 	saveFile.write(str(readLineFile[:][:limitColumn]) + "\n")
	# saveFile.close
	# readFile.close

