letra = 's'
while letra == 's':
    n1 = float(input('Digite o primeiro Valor: '))
    n2 = float(input('Digite o segundo Valor: '))
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Divisão")
    print("[4] Multiplicação")
    opcao = str(input('Qual opção deseja calcular:'))
    if opcao == '1':
        print('A soma é:', n1 + n2)
    elif opcao == '2':
        print('A subtração é:', n1 - n2)
    elif opcao == '3':
        print('A divisão é:', n1 / n2)
    elif opcao == '4':
        print('A multiplicação é:', n1 * n2)

    letra = input('Deseja continuar? [S/N]: ')