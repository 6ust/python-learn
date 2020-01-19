x = int(input("Escolha uma opcao: \n1 - Criar TXT\n2 - Leitura por terminal\n3 - Acrescentar informacoes\n4 - Informacoes do Arquivo\n0 - Sair\n\n"))

while x != 0:
	if x == 1:
		#Escrita de arquivo TXT
		with open('guardando-dados-python.txt','w') as fileW:
			fileW.write('dados de codigo python sendo armazenados em arquivo TXT\n\n')
			fileW.write('Sequencia de numeros aleatorios:\n')
			fileW.close()

		with open('guardando-dados-python.txt') as fileR:
			print(fileR.read())
			fileR.close()


	if x == 2:
		#Leitura de arquivo TXT
		fileR = open('guardando-dados-python.txt','r')
		for line in fileR:
			line = line.rstrip()
			print(line)

		fileR.close()


	if x == 3:
		#Acrescentar texto em arquivo TXT
		fileA = open('guardando-dados-python.txt','a')

		fileA.write('Acrescentando dados ao TXT\n\n')

		fileA.close()
	

	if x == 4:
		#Informacoes do arquivo TXT
		fileA = open('guardando-dados-python.txt','a')
		print("Informacoes do arquivo - Operacao concluida no arquivo " + fileA.name + " usando o modo de acesso " + fileA.mode)


	x = int(input("Escolha uma opcao: \n1 - Criar TXT\n2 - Leitura por terminal\n3 - Acrescentar informacoes\n4 - Informacoes do Arquivo\n0 - Sair\n\n"))

