print('\t--CARRITO DE LA COMPRA--')

producto1 = input('Producto:')
precio = float(input(f'Precio del {producto1}:'))
producto2 = input('Producto:')
precio += float(input(f'Precio del {producto2}:'))
producto3 = input('Producto:')
precio += float(input(f'Precio del {producto3}:'))

print(f'\t\nEl importe de su compra es {precio:.2f} euros (sin iva).')

if precio > 20 and precio <= 30:
    print('Tienes opción a un gran descuento si ingresas tu código postal')
    elegir = input('Y/N').upper()
    if elegir == 'Y':
        cp = int(input('Código postal: '))
        descuento = precio * 0.5
        print(f'\tSu descuentos es de {descuento:.2f} euros')
        preciodescuento = precio - descuento
    else:
        print('Usted se lo pierde')
        preciodescuento = precio

elif precio >= 50:
    descuento = precio * 0.5
    preciodescuento = precio - descuento
    print(f'\tSu descuento es de {descuento:.2f} euros')

else:
    print(f'No tiene descuento con esta compra de {precio:.2f} euros')
    precioSinIva= precio

iva = precio * 0.21
preciototal = preciodescuento + iva
print(f'\tSu iva es {iva:.2f}euros')
print(f'\tTu precio sin iva es {preciodescuento:.2f}euros')
print(f'\t\nEl importe final de su compra es {preciototal:.2f} euros.') #\n cambia de linea
