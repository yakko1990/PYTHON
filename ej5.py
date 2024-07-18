
numero = int(input("Dime un número positivo: "))
if numero < 0:
    numero = int(input("Dime un número positivo: "))


# suma = 0
# for i in range(1, numero + 1 ):
#     suma += i
# Otra posible solucion

suma = (numero *(numero + 1)) / 2

print("La suma de los números es " + str(suma))
