n1 = float(input("Digite sua altura: "))
n2 = float(input("Digite o seu peso: "))

imc = n2 / (n1 * n1)

print("o IMC será: ", imc)
print("A sua altura: ", n1)
print("Peso informado:", n2)

if imc >= 30:
    print("Cuidado com a saúde")
elif imc <= 25:
    print("Peso Normal")
