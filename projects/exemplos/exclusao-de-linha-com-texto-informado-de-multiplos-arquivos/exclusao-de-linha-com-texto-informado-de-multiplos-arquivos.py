# Descriptor: Automatização de Exclusao de Linha Com Texto Informado de Multiplos Arquivos
# Author:     Gust Guedes 

# Comandos do Sistema Operacional - OS 
import os
import sys
import shutil
import os.path

# RegEX
import re

# Variaveis de Construção e Identificação do Caminho
pathRead  = "./originais/"
newFolder = "atualizados" 
pathSave  = "./" + newFolder + "/"


# Inicialização do Sistema
print("\n\n")
print("ATENÇÃO NÃO COLOQUE SEUS ARQUIVOS NA PASTA: [atualizados]")
print("POIS ELA SERA ATUALIZADA!")
print("Coloque seus arquivos na pasta: [originais].")

# Limite de Coluna estabelecido para salvamento/Atualização
print("\n\n")
searchUser = str(input("O que gostaria de deletar do(s) Arquivo(s): "))
wait = input("pressione Enter para continuar")


#Verifica a existencia de um diretorio
if(os.path.isdir(pathSave)):
	# exclui um diretório e todo o seu conteúdo.
	shutil.rmtree(pathSave)

# Criar Diretorio
os.mkdir(pathSave)

print("\n\n")

fileDir = os.listdir(pathRead)
for file in fileDir:
	# Leitura de Documento/ Arquivo
	readFile = open(pathRead + file, "r", encoding="utf8")


	# Exibe o Nome do Arquivo
	print("------------------------------------")
	print(str(file) + " - Atualizado")

	# Salvamento de Documento/ Arquivo
	saveFile = open(pathSave + file, "a", encoding="utf8")
	for readLineFile in readFile:
		searchLine = re.search(searchUser,readLineFile)
		if(not searchLine):
			saveFile.write(str(readLineFile[:][:]))

	saveFile.close
	readFile.close
print("------------------------------------")
confirmExec = "exit"