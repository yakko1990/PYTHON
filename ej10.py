



inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance = inversion

for i in range(1, 4):
    balance *= (1 + interes)
    print(f"Balance tras el año {i}: {round(balance, 2)}")
