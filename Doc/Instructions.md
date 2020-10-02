Instrucciones:

En el diseño de las instrucciones se ha intentado mantener
libre los opcodes disponibles en la medida de lo posible para
posibilitar la introducción de nuevas instrucciónes en el futuro
haciendo los opcodes lo más largos posibles.

					D = Dirección
					I = Inmediato
					S = Bits de selección
					R = Registro de lectura
					W = Registro de escritura

noop:			0000 00XX XXXX XXXX: No toma operandos
jump:			0000 01DD DDDD DDDD: Salto a D
jumpz:		0000 10DD DDDD DDDD: Salto a D si flag Zero = 1
nojumpz:	0000 11DD DDDD DDDD: Salto a D si flag Zero = 0
limm:			0001 IIII IIII WWWW: Cargar I en W
jal:			0010 00DD DDDD DDDD: Salto a D guardando dir. retorno (PC + 1)
ret:			0010 01XX XXXX XXXX: No toma operandos
read:			0010 10SS XXXX WWWW: SS seleccionan el puerto de lectura
write:		0010 11SS RRRR XXXX: SS seleccionan el puerto de escritura
MOV:      1000 RRRR XXXX WWWW: Guarda R en W
NEG:      1001 RRRR XXXX WWWW: Niega R y guarda en W
ADD:			1010 RRRR RRRR WWWW: R1 + R2 -> W
SUB:			1011 RRRR RRRR WWWW: R1 - R2 -> W
AND:			1100 RRRR RRRR WWWW: R1 & R2 -> W
OR:				1101 RRRR RRRR WWWW: R1 | R2 -> W
SIGNA:		1110 RRRR XXXX WWWW: Cambia signo a R y guarda en W
SIGNB:		1110 XXXX RRRR WWWW: Cambia signo a R y guarda en W


E/S:
La entrada salida se compone de un banco de cuatro registros para la
salida en el que se escriben los datos y cuatro puertos de entrada.
La salida se compone unicamente de varios multiplexores y wires.
No se han implementado escritura de inmediatos para no gastar opcodes
y por ser menos flexibles que la escritura desde registro.

Timer:
El timer esta diseñado para tener una presición de 1ms al conectarse
a un relog de 24MHz. Es necesario pasarle un numero(8b) de ms que en 
el caso de esta cpu se envia por el puerto 0 y permite generar señales
periódicas de entre 1ms y 250ms.

Interrupciones:
La cpu permite 4 interrupciones externas que selecciónan una dirección
de memoria donde se deberá encontrar una subrutina que termine en una
instrucción ret que devuelva la ejecución del programa a su cauce normal.
Hasta que no implemente una pila para los JAL cualquier interrupción
sobrescribirá cualquier información presente en el registro de retorno.
