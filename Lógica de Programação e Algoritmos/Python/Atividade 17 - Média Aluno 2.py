letra = 's'
while letra == 's':

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira: "))

    soma = nota1 + nota2 + nota3
    media = soma / 3

    print(f"A média do aluno é: {round(media, 2)}")

    if media >= 7:
        print("Aprovado")
    elif media >= 3:
        print("Recuperação")
    else:
        print("Reprovado")

    letra = input('Deseja continuar? [S/N]: ')