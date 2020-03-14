# Comandos do Sistema Operacional - OS 
import os
import sys
import shutil


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

# exclui um diretório e todo o seu conteúdo.
shutil.rmtree(pathSave)

# Criar Diretorio
os.mkdir(pathSave)


fileDir = os.listdir(pathRead)
for file in fileDir:
	print(fileDir)

	# Leitura de Documento/ Arquivo
	readFile = open(pathRead + file, "r", encoding="utf8")


	# Exibe o Nome do Arquivo
	print("------------------------------------")
	print(file)
	print("------------------------------------")


	# Leitura por linhas do Documento
	# Salvamento de Documento/ Arquivo
	print(pathSave + file)
	saveFile = open(pathSave + file, "a", encoding="utf8")
	for readLineFile in readFile:
		saveFile.write(str(readLineFile[:][:limitColumn]) + "\n")
	saveFile.close
	readFile.close

