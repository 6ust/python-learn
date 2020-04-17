# LISTAGEM DE TODOS OS ARQUIVOS DE UM DIRETORIO

#REFERENCIA
# https://mkyong.com/python/python-how-to-list-all-files-in-a-directory/

import os

pathFiles = 'C:\\Users\\gustavoguedes\\Documents\\programming-language\\python\\ambiente-de-testes-brq\\listagem-de-arquivos-de-um-diretorio\\th\\'

files = []

# r = Root, d = Directories, f = Files
for r, d, f in os.walk(pathFiles):
	for file in f:
		if  '' in file:
			files.append(os.path.join(r, file))

for f in files:
	print(f[len(pathFiles):])