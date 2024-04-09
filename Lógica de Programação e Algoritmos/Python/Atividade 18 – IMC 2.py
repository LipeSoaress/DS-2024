n1 = float(input("Digite sua altura: "))
n2 = float(input("Digite o seu peso: "))

imc = n2 / (n1 * n1)

print(f'O IMC dessa pessoa é: {round(imc, 2)}')

if imc < 18.4:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso Normal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade grau 1")
elif imc <= 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")