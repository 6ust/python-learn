
# Leitura de Documento/ Arquivo
readFile = open("teste", "r", encoding="utf8")
# readFile = open("testes.txt", "r", encoding="utf8")

# Esta função apenas acrescenta linhas ao final do Arquivo
saveFile = open("testes1.txt", "a", encoding="utf8")

# Limite de Coluna estabelecido para salvamento/Atualização
limitColumn = 78

print("------------------------------------")

# Leitura por linhas do Documento
for readLine in readFile:

	print(readLine[:][:limitColumn])

	# salvamento ao final do arquivo
	saveFile.write(str(readLine[:][:limitColumn]) + "\n")

	print("------------------------------------")

readFile.close
saveFile.close
