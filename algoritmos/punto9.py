monto_inicial = int( input('Monto inicial de la tarjeta: ') )
monto_final = int( input('Monto final de la tarjeta: ') )

consumo_tarjeta = monto_inicial - monto_final
costo_llamada = consumo_tarjeta + ( consumo_tarjeta * 0.2 )

print( F'Coste de la llamada { costo_llamada } ' )