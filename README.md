asm2binary
==========
[English version will follow]

Transforme du code assembler en instruction binaire pour le processeur à usage
multiple du cours INF3500 à Polytechnique Montréal

Par Francis Deslauriers et Anthony Buffet

N.B.
Bugs connus (Les patchs sont les bienvenues pour ces problèmes): 
- ~~Le programme plante  si il y a un commentaire sur même ligne que label~~ Merci [David Albertson](https://github.com/Diastro)
- ~~Le programme plante  si il y a un ligne vide~~ Merci [David Albertson](https://github.com/Diastro)
- Le programme plante  si il y a un chargement d'une valeur négative dans un registre.

Par Francis Deslauriers et Anthony Buffet

--English--

Compile assembly code into binary instruction that are understood by the VHDL multi-usage CPU designed during the digital circuit design class (INF3500) at Polytechnique Montréal.


N.B.
Known bugs (Patches are welcome): 
- ~~Crash if comment on the same line of label~~ Thanks [David Albertson](https://github.com/Diastro)
- ~~Crash if empty line~~ Thanks [David Albertson](https://github.com/Diastro)
- Crash if negative value is loaded in a register.

By Francis Deslauriers and Anthony Buffet


Instructions:
- jmp : Saut inconditionnel / unconditionnal jump	
- jz : Saut si derniere soustraction = 0 / Jump if last substraction is equals to zero	
- jdz : Saut si derniere soustraction != 0 / Jump if last substraction is not equals to zero	
- jn : Saut si derniere soustraction negatif / Jump if the result of the last substract	is below zero
- jp : Saut si derniere soustraction positif / Jump if the result of the last substract	is above zero
- rext : Lis dans la mémoire externe / Read from external memory
- wext : Écrit dans la mémoire externe / Write to external memory
- rmem : Lis mémoire interne / Read from internal memory
- wmem : Écrit dans memoire interne / Write to external memory
- mov : Charge une valeur dans un registe / Load value into register
- add : Addition deux registres / Add to registers
- sub : Soustrait deux registres / Substract to registers

Exemple/example : 
<pre><code>
mov r1 99
jz allo
francis:
jn francis
jp francis
add r3 r3 r2
sub r2 r1 r2
test:
rmem r1 r2 #Comment2
wmem r5 r8 #Comment1
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
	x"80102ff", --rmem r1 r2 #Comment2
	x"9FF0508", --wmem r5 r8 #Comment1
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
	
	
