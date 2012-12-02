asm2binary
==========

Transforme du code assembler en binaire

N.B.
Bugs connus : 
		Commentaire sur même ligne que label
		
		Ligne vide
		
		Charger dans un registre une valeur négative

Instructions:
	jmp : jump inconditionnel
	
	jz : jump si derniere soustraction = 0
	
	jdz : jump si derniere soustraction != 0
	
	jn : jump si derniere soustraction negatif
	
	jp : jump si derniere soustraction positif
	
	