
inversion = float(input('Introduce la cantidad a invertir: '))
numAños = int(input('Introduce la cantidad de años: '))
interesAnual = float(input('Introduce el interes Anual: '))


capital = inversion


for i in range(numAños): 
    capital *= (1 + interesAnual / 100)

print('El capital total obtenido en la inversión es de ' + str(round(capital, 2)))
