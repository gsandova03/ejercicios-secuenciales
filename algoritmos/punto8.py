horas_trabajadas = int( input('Horas trabajadas: ') )

pago = horas_trabajadas * 20000
descuento = pago * 0.005
pago_total = pago - descuento

print( F'Pago total al profesor { pago_total } y descuento por ahorro { descuento }' )