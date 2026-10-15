lado1 = float(input ("Escribe el primer lado"))
lado2 = float(input("Escribe el segundo lado"))
lado3 = float(input("Escribe el tercer lado"))

if lado1==lado2 and lado2==lado3:   #corrección
    print("Equilátero")

elif lado1 == lado2 or lado1==lado3 or lado2 == lado3: 
    print("Isósceles")

else:
    print("Escaleno")   