asm2binary
==========

Transforme du code assembler en binaire

N.B.
Bugs connus (Les patchs sont les bienvenues pour ces problèmes): 
- Le programme plante  si il y a un commentaire sur même ligne que label
- Le programme plante  si il y a un ligne vide
- Le programme plante  si il y a un chargement d'une valeur négative dans un registre

Instructions:
- jmp : jump inconditionnel	
- jz : jump si derniere soustraction = 0	
- jdz : jump si derniere soustraction != 0
- jn : jump si derniere soustraction negatif	
- jp : jump si derniere soustraction positif
- rext : lis dans la mémoire externe
- wext : écrit dans la mémoire externe
- rmem : lis mémoire interne
- wmem : ecrit dans memoire interne

Exemple : 
<pre><code>
mov r1 99
jz allo
francis:
jn francis
jp francis
add r3 r3 r2
sub r2 r1 r2
test:
rmem r1 r2 #Commentaire2
wmem r5 r8 #Commentaire1
rext r1
wext r5
mov r0 0
allo:
mov r2 3
mov r5 0
curly:
wmem r0 r2
add r0 r0 r1
sub r6 r4 r0
jp curly
jdz allo
rmem r0 r4
rmem r2 r5
jmp test
</code></pre>

Resultat :

<pre><code>
(	x"A010063", --mov r1 99
	x"C01F00b", --jz allo
	x"C03F002", --jn francis
	x"C04F002", --jp francis
	x"0030302", --add r3 r3 r2
	x"1020102", --sub r2 r1 r2
	x"80102ff", --rmem r1 r2 #allo
	x"9FF0508", --wmem r5 r8 #sdasa
	x"D01ffff", --rext r1
	x"Effff05", --wext r5
	x"A000000", --mov r0 0
	x"A020003", --mov r2 3
	x"A050000", --mov r5 0
	x"9FF0002", --wmem r0 r2
	x"0000001", --add r0 r0 r1
	x"1060400", --sub r6 r4 r0
	x"C04F00d", --jp curly
	x"C02F00b", --jdz allo
	x"80004ff", --rmem r0 r4
	x"80205ff", --rmem r2 r5
	x"C00F006", --jmp test	others => (others => '1'));
</code></pre>
	
	