print("\nCriação de Arrays")
print("----------------------------------")

# Create array in python
sons = ["Micheal","Laura","Brian","Maxwell","Lily"]

# Show elements array
for arrayCount in sons:
	print(arrayCount)

print("\nAdicionado Elementos")
print("----------------------------------")

# adding new elements in array
sons.append("Dylan")
sons.append("Sophie")
sons.append("Gean")

# Show elements array
for arrayCount in sons:
	print(arrayCount)

print("\nRemovendo Elementos")
print("----------------------------------")
sons.pop(7)