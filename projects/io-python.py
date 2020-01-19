# Input with cast transform string in integer
limit = int(input("Defina um limite para a geração de sequencia aleatoria "))

count = 0
while count <= limit:
	print("numero -> " + str(count) + " de " + str(limit))
	count += 1