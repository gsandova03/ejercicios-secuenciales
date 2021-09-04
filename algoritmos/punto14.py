cantidad_dias = int( input('Cantidad de dias: ') )

valor_total = 0

for i in range( cantidad_dias ):
  if( i == 0 ):
    valor_total += 100000

  if( i >= 1 ):
    valor_total += 200000

print( f'Valor total a pagar { valor_total }' )