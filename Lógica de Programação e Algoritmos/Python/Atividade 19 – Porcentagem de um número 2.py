letra = 's'
while letra == 's':

    valor = float(input("valor: "))
    pp = float(input("porcentagem: "))

    resultado = valor * (pp / 100)

    print(resultado)

    letra = input('Deseja continuar? [S/N]: ')