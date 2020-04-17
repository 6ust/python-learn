# RegEX
import re

searchUser = str(input("TESTAR: "))
# searchUser = "\Mi!necr?a.ft,"
# searchUser = ".minecraft"
example =  "a ,pasta de testes! ?é a: .minecraft e a .hta"

print("SEARCH AFTER --> " + searchUser)
print()

#-----------------------------------
#TRATAMENTO DE CARACTERES ESPECIAIS
#-----------------------------------
#Tratados
#[\][,][.][?]
searchUserRegExApplied = searchUser
# Tratamentos Prioritarios
if re.search(r"\\", searchUser):
	searchUserRegExApplied = re.sub(r"\\", r"\\\\", searchUserRegExApplied)

# Tratamentos Secundarios
if re.search(r"\.", searchUser):
	searchUserRegExApplied = re.sub(r"\.", r"\.", searchUserRegExApplied)
if re.search(r"\,", searchUser):
	searchUserRegExApplied = re.sub(r"\,", r"\,", searchUserRegExApplied)
if re.search(r"\?", searchUser):
	searchUserRegExApplied = re.sub(r"\?", r"\?", searchUserRegExApplied)
#-----------------------------------


# TESTES
# searchUserRegExApplied = re.sub(r"\\", r"POPO", searchUserRegExApplied)

if re.search(searchUserRegExApplied, example):
	print("Encontrei o Erro!")
print("SEARCH REGEX APPLIED --> " + searchUserRegExApplied)


# Possibilidades de Entrada em RegEx
# [/][!][_][=][|]
# 


#Aceitos
#[.][,][!][\]

#Não Aceitos
#[?] [\]

# Interpretação RegEx
#   \ = "\\\\"
#   ? = "\?"
