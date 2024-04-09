letra = 's'
while letra == 's':

    n1 = float(input('Qual o valor: '))
    tx = float(input('A Taxação Atual: '))
    print("[1] Real para Dolar")
    print("[2] Dolar para Real")
    inf = float(input('Qual será a conversão? '))

    if inf == 1:
        print("USD: ", (n1 / tx))
    else:
        print("BRL: ", (tx * n1))

    letra = input('Deseja continuar? [S/N]: ')