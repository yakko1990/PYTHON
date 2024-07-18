
payasos = 112
muñecas = 75


totalPayasos = int(input('Introduce la cantidad de payasos vendidos en el ultimo pedido '))
totalMuñecas = int(input('Introduce la cantidad de muñecas vendidas en el ultimo pedido '))

pesoPaquete = ((payasos * totalPayasos) + (muñecas * totalMuñecas))

if pesoPaquete > 1000:
    pesoPaquete = pesoPaquete /1000
    
print('El peso del paquete es de:', str(round(pesoPaquete,2)), 'kg')