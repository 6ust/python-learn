import json
from openpyxl import load_workbook, Workbook


print()
with open('json/people.json') as json_file:
    data = json.load(json_file)
    for p in data["people"]:
        print("Added in Sheet - " + p["nome"])
		# lista.append(p["nome"])



arquivo_excel = Workbook()
plan1 = arquivo_excel.active
# for p in lista:
	# plan1.append(p)
	# print(p)

arquivo_excel.save("exemplo.xlsx")
print("Planilha atualizada com Sucesso!")

