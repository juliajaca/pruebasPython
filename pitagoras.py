#teorema de pitágoras
'''
Ecuación de Pitágoras
Realizaremos una inmersión de código
En variables estructurales
'''

#la suma de los cuadrados de los catetos es igual al cuadrado de la hipotenusa

#cateto1= float(input('cateto1: '))

#cateto2 = float(input('cateto2: '))

#cuadrado_hipotenusa = (cateto1**2) + (cateto2**2)

#print(f'El cuadrado de la hipotenusa es: {cuadrado_hipotenusa:.2f} ')
## el :.2f te saca DOS decimales en el resultado


#######################################
# segunda ecuación

# a= float(input('a: '))

# b = float(input('b: '))

# resultado = (a**2/ 2 + 8) * (5**2 / (b**3 -7))

# print(f'El resultado es: {resultado:.2f} ')

#####################################
'''
# SACAR LA LONGITUD Y AREA de una circunferencias

Área = pi r cuadrado
Longitud = 2 pi r

'''

#Traemos la librería de matemáticas con pi

# import math

# radio = float(input('radio ->'))

# area = math.pi * radio**2
# longitud = 2 * math.pi * radio

# print(f'Si el radio es: {radio:.2f}, el area tiene que ser {area:.2f} y la longitud es {longitud:.2f}')

##################################################################TORTUGUITA

import turtle

lienzo = turtle.Screen() #generamos un lienzo para pintar
tortuguita = turtle.Turtle()

tortuguita.forward(100)
tortuguita.left(90)

tortuguita.forward(100)
tortuguita.left(90)

tortuguita.forward(100)
tortuguita.left(90)

tortuguita.forward(100)
tortuguita.left(90)

turtle.mainLoop() ##retiene la ventana
