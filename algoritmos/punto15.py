monto_prestamo = int( input('Cantida prestada: ') )

valor_final = monto_prestamo + ( monto_prestamo * 0.24 )
mitad_prestamo = monto_prestamo / 2
cuotas_especiales = mitad_prestamo / 4
cuotas_ordinarias = mitad_prestamo / 20

print(f'Resumen del prestamo, valor final { valor_final }, valor cuotas especiales { cuotas_especiales } y valor cuotas ordinarias { cuotas_ordinarias }')