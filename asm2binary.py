#! /usr/bin/python
import sys
def trouverEtiquettes(content):
	dictionnaire = {}

	compteLabel = 0
	compteLigne = 0

	for i in content:
		if i[len(i)-2] == ':': # c'est une label
			dictionnaire[i[0:len(i)-2]] = compteLigne-compteLabel
			compteLabel = compteLabel + 1

		compteLigne = compteLigne + 1
	return dictionnaire




def analiserLigneHexa(li, diction):    #
	op = li.split()
# on ignore les commentaires
	for j in op:
		if j[0] == '#':
			op.remove(j)


	instruction = bin(1)
	operandes = [None]*10



	if op[0] == 'mov': # charge en memoire
		operandes[0] = str("0xA"[2:])
		operandes[1] = str(hex(int(op[1][1:]))[2:].zfill(2))
		operandes[2] = str(hex(int(0))[2:].zfill(2))
		operandes[3] = str(hex(int(op[2]))[2:].zfill(2))
	elif op[0] == 'jmp': #jmp non conditionnel
		operandes[0] = str("0xC"[2:].zfill(1))
		operandes[1] = str(hex(0x0)[2:].zfill(2))
		addresLabel = diction[op[1]]
		addr = str(hex(addresLabel)[2:].zfill(3))
		operandes[2] = "F"+addr[0]
		operandes[3] = addr[1]+addr[2]
	elif op[0] == 'jz': #egal a zero
		operandes[0] = str("0xC"[2:].zfill(1))
		operandes[1] = str(hex(0x1)[2:].zfill(2))
		addresLabel = diction[op[1]]
		addr = str(hex(addresLabel)[2:].zfill(3))
		operandes[2] = "F"+addr[0]
		operandes[3] = addr[1]+addr[2]
	elif op[0] == 'jdz': #different de zero
		operandes[0] = str("0xC"[2:].zfill(1))
		operandes[1] = str(hex(0x2)[2:].zfill(2))
		addresLabel = diction[op[1]]
		addr = str(hex(addresLabel)[2:].zfill(3))
		operandes[2] = "F"+addr[0]
		operandes[3] = addr[1]+addr[2]
	elif op[0] == 'jn': #negatif
		operandes[0] = str("0xC"[2:].zfill(1))
		operandes[1] = str(hex(0x3)[2:].zfill(2))
		addresLabel = diction[op[1]]
		addr = str(hex(addresLabel)[2:].zfill(3))
		operandes[2] = "F"+addr[0]
		operandes[3] = addr[1]+addr[2]
	elif op[0] == 'jp': #positif
		operandes[0] = str("0xC"[2:].zfill(1))
		operandes[1] = str(hex(0x4)[2:].zfill(2))
		addresLabel = diction[op[1]]
		addr = str(hex(addresLabel)[2:].zfill(3))
		operandes[2] = "F"+addr[0]
		operandes[3] = addr[1]+addr[2]
	elif op[0] == 'add': #add
		operandes[0] = str("0x0"[2:].zfill(1))
		operandes[1] = str(hex(int(op[1][1:]))[2:].zfill(2))
		operandes[2] = str(hex(int(op[2][1:]))[2:].zfill(2))
		operandes[3] = str(hex(int(op[3][1:]))[2:].zfill(2))
	elif op[0] == 'sub': #sub
		operandes[0] = str("0x1"[2:].zfill(1))
		operandes[1] = str(hex(int(op[1][1:]))[2:].zfill(2))
		operandes[2] = str(hex(int(op[2][1:]))[2:].zfill(2))
		operandes[3] = str(hex(int(op[3][1:]))[2:].zfill(2))
	elif op[0] == 'rmem': #read memory r1 = desti, r2 = addresse dans memoire
		operandes[0] = str("0x8"[2:].zfill(1))
		operandes[1] = str(hex(int(op[1][1:]))[2:].zfill(2))
		operandes[2] = str(hex(int(op[2][1:]))[2:].zfill(2))
		operandes[3] = str(hex(int(0xFF))[2:].zfill(2))
	elif op[0] == 'wmem': #write memory r1 = source , r2 = addresse dans memoire
		operandes[0] = str("0x9"[2:].zfill(1))
		operandes[1] = str("0xFF"[2:].zfill(2))
		operandes[2] = str(hex(int(op[1][1:]))[2:].zfill(2))
		operandes[3] = str(hex(int(op[2][1:]))[2:].zfill(2))
	elif op[0] == 'rext': #read external memory r1 = desti
		operandes[0] = str("0xD"[2:].zfill(1))
		operandes[1] = str(hex(int(op[1][1:]))[2:].zfill(2))
		operandes[2] = str(hex(int(0xFF))[2:].zfill(2))
		operandes[3] = str(hex(int(0xFF))[2:].zfill(2))
	elif op[0] == 'wext': #write external memory r1 = source 
		operandes[0] = str("0xE"[2:].zfill(1))
		operandes[1] = str(hex(int(0xFF))[2:].zfill(2))
		operandes[2] = str(hex(int(0xFF))[2:].zfill(2))
		operandes[3] = str(hex(int(op[1][1:]))[2:].zfill(2))

	instruction = operandes[0]+operandes[1]+operandes[2]+operandes[3]	
	return instruction



fichier = open(sys.argv[1])
content = fichier.readlines()
diction = trouverEtiquettes(content)
vecteur = "("
for i in content:
	if i[len(i)-2] == ':':
		print ("Etiquette detectee")
	else:
		instruc = analiserLigneHexa(i,diction)
		vecteur = vecteur+ "\tx\""+instruc+"\", --"+i

vecteur = vecteur + "\tothers => (others => \'1\'));"
print (vecteur)