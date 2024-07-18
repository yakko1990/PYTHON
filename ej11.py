pan = 3.49
descuento = 0.60

panReceso = int(input("Cuantos panes que no son del dia se han vendido hoy "))
print("el precio de una barra es " + str(pan))
print("el descuento por no ser fresca es de " + str((descuento * 100)))
print("el coste final total es de " + str((pan * panReceso)))