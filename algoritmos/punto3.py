persona1 = int(input("Primera persona: "))
persona2 = int(input("Segunda persona: "))
persona3 = int(input("Tercera persona: "))

total = persona1 + persona2 + persona3

porPersona1 = persona1 / total
porPersona2 = persona2 / total
porPersona3 = persona3 / total


print( F' {porPersona1 * 100} % ' )
print( F' {porPersona2 * 100} % ' )
print( F' {porPersona3 * 100} % ' )