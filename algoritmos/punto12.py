total_peliculas = int( input('Peliculas alquiladas: ') )
num_dias_alquiler = int( input('Dias de alquiler: ') )

if( total_peliculas >= 2 ):
  pago_alquiler = num_dias_alquiler * 1500
  pago_total = ( total_peliculas - 1 ) * pago_alquiler
  print( f'Total monto a pagar { pago_total }' )
elif( total_peliculas == 1 ):
  pago_alquiler = num_dias_alquiler * 1500
  pago_total = total_peliculas * pago_alquiler
  print( f'Total monto a pagar { pago_total }' )
