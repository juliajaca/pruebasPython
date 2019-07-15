# IF, CONDICIONAL

if 10 > 0:
    print('esto es un if')
    print('otra linea')
elif 10 == 0:
    print(' esto se parece a else if')
else:
    print(' esto es un else')

# #IF anidado

edad = int(input('¿Cuál es tu edad?'))

if 0 < edad < 120 : #  es lo mismo que edad >=0  and edad < 120
    print('La introducción de datos es correcta')
    if edad >=18:
        print('Eres mayor de edad')
    if edad < 18:
        print(' Eres un pitufino')
else:
    print('Te has equivocado con la introducción de la edad')


##EJERCICIO VER EL QUE TIENE MAS EDAD
nombre1 = input('¿Cuál es tu nombre, persona 1?')
edad1 = int(input('¿Cuál es tu edad, persona 1?'))

nombre2 = input('¿Cuál es tu nombre, persona 2?')
edad2 = int(input('¿Cuál es tu edad, persona 2?'))

nombre3 = input('¿Cuál es tu nombre, persona 3?')
edad3 = int(input('¿Cuál es tu edad, persona 3?'))

if edad1> edad2 and edad1>edad3:
    print(f'EL mayor es {nombre1}')
    diferenciacon2 = edad1 - edad2
    diferenciacon3 = edad1 - edad3
    print(f'Y gana a {nombre2} de {diferenciacon2}años')
    print(f'Y gana a {nombre3} de {diferenciacon3}años')

if edad2> edad1 and edad2>edad3:
    print(f'EL mayor es {nombre2}')
    diferenciacon1 = edad2 - edad1
    diferenciacon3 = edad2 - edad3
    print(f'Y gana a {nombre1} de {diferenciacon1}años')
    print(f'Y gana a {nombre3} de {diferenciacon3}años')

if edad3> edad2 and edad3>edad1:
    print(f'EL mayor es {nombre3}')
    diferenciacon1 = edad3 - edad1
    diferenciacon2 = edad3 - edad2
    print(f'Y le lleva a  {nombre1} {diferenciacon1}años')
    print(f'Y le lleva a  {nombre2} {diferenciacon2}años')


#SWITCH NO EXISTE

c = input('Insertar una letra').lower() #inserta la letra en minuscula
if c  == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
    print('esto es una vocal')
else:
    print('esto no es una vocal')


