numero1 = float(input('¿Cuál es tu primer número?'))
numero2 = float(input('¿Cuál es tu segundo número?'))
operacion = str(input('OPERADOR (S/M/D/R)')).upper()


if operacion == 'S':
    resultado = numero1 + numero2

if operacion == 'M':
    resultado = numero1 * numero2

if operacion == 'D':
    resultado = numero1 / numero2

if operacion == 'R':
    resultado = numero1 - numero2

print(f'El resultado es {resultado}')
    