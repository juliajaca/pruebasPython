# Variables
# *********************************


# nombre = 'Toni'
# print(nombre)


#*************************************
#CAlcular el area de un circulo
# pi= 3.1415
# radio = 3

# area = pi * radio **2

# print(area)
#***********************************************************
# nombre = 'julia'
# apellido =' aaa'

# print ('Mi nombre es '+ nombre+ ' y mi primer apellido' + apellido)

#****************************************
#entrada de datos
#nombre = raw_input('¿Cuál es tu nombre?') #esto funicona en la version 2, pero no en la 3
# nombre = str(input('¿Cuál es tu nombre?')) #esto funcina en la version 3
#         #el dato que nos meta lo convierte en string, porque el + solo encadena str. En cambio si no pones nada, te lo hace string automaticamente, pero asi vemos como podemos transformar el tipo de datos con el input
# print(type (nombre))
# print('hola ' + nombre)


# ********************************
# Prioridades de operadores genéricos

# 1. Paréntesis de dentro a afuera
# 2. Potencias
# 3. Multiplicaciones, divisiones, módulos y not
# 4. Sumas , restas y and
# 5. Mayor, menor, igual, mayor o igual, menor o igual, diferente, y or


#Operadores de asignación

# a = 0

# a += 5
# a = a + 5

# a -= 5

# a*= 4

# a/=5

# a** = 9

# a%=4


#CONCATENAR CON STRING Y VARIABLES
# nombre = 'Toni'
# altura = 1.86

#primera opción : la coma es el concatenado genérico, deja un espacio por defecto
# print('hola me llamo',nombre,'y mido',altura,'metros de estatura')

# #segunda opción de Python 2
# #print('hola me llamo {} y mido {} metros de estatura').format(nombre, altura)

# #Tercera opción
# print(f'Hola me llamo {nombre} y mido {altura} metros de estatura')

# print(f'Hola me llamo {nombre}'
#     f' y mido {altura} metros de estatura')


#ENTRADA DE DATOS
#input te guarda datos tipo cadena

# nombre= input('Tu nombre: ')

# #input guardar valores numericos
# edad= int(input('Tu edad: '))
# altura = float(input('Tu altura: ')) #esto es como el double de mysql. EN php se llama float también

# print(f'Hola tu {nombre} y tu edad es {edad}, como tu altura {altura} metros')

#**********************************************************************
#FUnciones integradas

#convertir un strin a un entero
n = int('29')

#convertir un string a decimal
n = float ('10.4')

#convertir un numero a string
n = str(10)

#convertir un número a binario
n = bin(10) 

#convertir un número a hezadecimal
n = hex(10)

#convertir un bnario a entero
n = int('0b1010' , 2) # especifico el dos al final porque es un binario

#convertir hexadecimal a entero
n = int('0xa' , 16) #hexacimal es 16

#convertir un negativo a un positivo
n = abs(-12)

#convertir de número decimal a entero
n = round(4.8)

#cuenta cantidad de caracteres
n = len('Tonia')