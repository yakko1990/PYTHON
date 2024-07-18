
peso = float(input('Dime tu peso en kg: '))
altura = float(input('Dime tu altura en metros: '))


imc = peso / (altura ** 2)

imc_redondeado = round(imc, 2)


print(f'Tu IMC es de: {imc_redondeado}')
