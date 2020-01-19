# https://pt.stackoverflow.com/questions/195422/gerar-n%C3%BAmeros-aleat%C3%B3rios-em-python-sem-repetir
# Algorith to Stackoverflow

# program by sequency of numbers random
from random import randint

# Create array
seqN = []
count = 0

limitSeqN = int(input("Informe um limite para a sequencia: \n"))

# Algorithim generate random sequency numbers
while len(seqN) != limitSeqN:
    numRand = randint(0, limitSeqN - 1)
    if numRand not in seqN:
        seqN.append(numRand)

 # Show elements array
for arrayCount in seqN:
	print(arrayCount)