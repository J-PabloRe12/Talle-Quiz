matricula  = float(input("Ingrese el valor de la matricula: "))
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))

promedio = (nota1+nota2+nota3+nota4)/4
print(f"Tu promedio es: {promedio}")

descuentoMatricula = matricula*0.8

if 4 <= promedio <= 5:
    print(f"Como tu promedio es {promedio} tienes un descuento del 20% y la matricula te queda en: {descuentoMatricula}")
elif 3 <= promedio <= 3.99:
    print(f"Tu promedio es {promedio} y el valor de tu matrícula es:{matricula}")
elif 0 <= promedio <= 2.99:
    print(f"Tu promedio es {promedio} y el valor de tu matrícula es:{matricula}")

else:
    print("Valor incorrecto")
