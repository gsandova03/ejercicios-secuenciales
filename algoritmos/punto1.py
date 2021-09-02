pre = int(input("presion: "))
vol = int(input("volumen: "))
temp = int(input("temperatura: "))

masa = float(( pre * vol ) / ( 0.37 * (temp + 460) ))
print( masa )