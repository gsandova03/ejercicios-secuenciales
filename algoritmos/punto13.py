cant_personas = int( input('Cantidad de personas: ') )

total = cant_personas * 25000
total_iva = total + ( total * 0.12 )

print( f'Valor total por paseo mas el iva { total_iva }' )