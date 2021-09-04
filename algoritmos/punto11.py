presupuesto = int( input('Monto presupuestal: ') )

area_ginecologia = presupuesto * 0.4
area_traumatologia = presupuesto * 0.3
area_pediatria = presupuesto * 0.3

print( f'Presupuesto para cada area, gin { area_ginecologia }, trauma { area_traumatologia } y pedia { area_pediatria }' )