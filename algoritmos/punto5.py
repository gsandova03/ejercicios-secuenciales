sueldo = int( input( "Sueldo: " ) )

politica = float( sueldo - ( sueldo * 0.01 ))
seguro = float( sueldo - ( sueldo * 0.04 ))
seguroFor = float( sueldo - ( sueldo * 0.005 ))
ahorro = float( sueldo - ( sueldo * 0.05 ))
total_a_pagar = float( sueldo - politica - seguro - seguroFor - ahorro )

print( F' total a pagar { total_a_pagar } y descuentos { politica }, { seguro }, { seguroFor }, { ahorro } ' )