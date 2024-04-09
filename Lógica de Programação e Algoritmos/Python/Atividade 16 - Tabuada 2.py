letra = 's'
while letra == 's':

    inicio = int(input("Tabuada de qual número? "))
    fim = int(input("Começar a tabuada com qual valor? "))
    t = int(input("Fazer a tabuada até qual valor? "))

    for i in range(fim, t+1):
        print(inicio*i)

    letra = input('Deseja continuar? [S/N]: ')