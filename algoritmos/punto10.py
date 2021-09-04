num_fotos = int( input('Numero de fotos: ') )

total = num_fotos * 1500
total_iva = total + ( total * 0.16 )

print( f'Cuenta total con IVA { total_iva }' )