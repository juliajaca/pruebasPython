# saldo inicial 4000 euros
# funciones de ingresar, retirar, mostrar y salir


#dinero en el cajero
saldo = 4000.54

#interface gráfica
print('\t--MENU--')
print('1. Ingresar dinero en la cuenta')
print('2. Retirar dinero en la cuenta')
print('3. Ver dinero en la cuenta')
print('4. Salir')
print('') #<br>

#print('Tus opciones son Ingresar dinero (I), sacar dinero(S), mostrar saldo (M), y salir (E)')
operacion = int(input('Elige una opción del menú'))

if operacion == 1 or operacion == 2:
    cantidad = float(input('¿Qué cantidad?'))
    if operacion == 2:
        if cantidad > saldo:
            print('No tiene suficiente dinero')
        else:
            saldo = saldo - cantidad
            print(
                f'Va a retirar {cantidad:.0f} euros.\n '
                f'Su saldo es ahora de {saldo:.2f} euros'
            )
    elif operacion == 1:
        saldo = saldo + cantidad
        print(
            f'Va a ingresar {cantidad:.0f} euros. \n'
            f'Su saldo es ahora de {saldo:.2f} euros'
        )

elif operacion == 3:
    print(
        f'Su saldo es de {saldo:.2f} euros. '
    )

elif operacion == 4:
    print(
        'Gracias por usar nuestros servicios'
    )
else:
    print('Error, se equivocó de opción en el menú')