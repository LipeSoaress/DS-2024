idd = int(input('Qual é a Idade do Jogardor: '))
if idd <= 13:
    print('Sua Categoria é infantil')
elif idd <= 17:
    print('Sua Categoria é juvenil')
elif idd > 17:
    print('Sua Categoria é Sênior')