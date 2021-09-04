num_palabras = int( input( "Numero de palabras: " ) )
tamano = int( input( "Tamaño en centimetros: " ) )
num_colores = int( input( "Numero de colores: " ) )

total_palabras = num_colores * 20000
total_tamano = tamano * 15000
total_colores = num_colores * 25000

suma_total = total_palabras + total_tamano + total_colores

print( F'Costo total del aviso { suma_total }' )