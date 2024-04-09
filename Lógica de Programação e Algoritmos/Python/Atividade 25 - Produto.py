from click import clear
nome_p = []
valor_p = []
descricao_p = []
quantidade_p = []
"""
letra = 's'
while letra == 's':
    clear()
    nome = input('Digite o nome do produto: ')
    valor = float(input('Valor do produto: '))
    quantidade = int(input('Quantidade de produtos: '))
    descricao = input('Descrição do produto: ')

    nome_p.append(nome)
    valor_p.append(valor)
    quantidade_p.append(quantidade)
    descricao_p.append(descricao)

    letra = input('Deseja continuar? [s/n]')

clear()

opcao = input('Deseja exibir os produtos? [sim/não]')
if opcao == 'sim':
    print("Nome do produto \t Valor do produto \t Quantidade  \t Descrição do produto")
    for lipe in range(0, len(nome_p)):
        print(f'{nome_p[lipe]} \t\t\t\t {valor_p[lipe]} \t\t\t\t\t {quantidade_p[lipe]} \t\t\t\t {descricao_p[lipe]}')
clear()

opc = input('Deseja excluir os produtos? [sim/não]')
if opc == 'sim':
    inf = int(input('Qual deseja excluir: '))
    if inf == inf:
        nome_p.pop(inf), quantidade_p.pop(inf), descricao_p.pop(inf), valor_p.pop(inf)
clear()

opcao = input('Deseja exibir os produtos? [sim/não]')
if opcao == 'sim':
    print("Nome do produto \t Valor do produto \t Quantidade  \t Descrição do produto")
    for lipe in range(0, len(nome_p)):
        print(f'{nome_p[lipe]} \t\t\t\t {valor_p[lipe]} \t\t\t\t\t {quantidade_p[lipe]} \t\t\t\t {descricao_p[lipe]}')
"""
def adicionar_produtos():
        nome = input('Digite o nome do produto: ')
        valor = float(input('Valor do produto: '))
        quantidade = int(input('Quantidade de produtos: '))
        descricao = input('Descrição do produto: ')

        nome_p.append(nome)
        valor_p.append(valor)
        quantidade_p.append(quantidade)
        descricao_p.append(descricao)

        with open('produtos.txt', 'a') as arquivo:
            arquivo.write(f'Nome: {nome}, Valor: {valor}, Quantidade: {quantidade}, Descrição: {descricao}\n')

def mostrar_produtos():
    print("Nome do produto \t Valor do produto \t Quantidade  \t Descrição do produto")
    for lipe in range(0, len(nome_p)):
        print(f'{nome_p[lipe]} \t\t\t\t {valor_p[lipe]} \t\t\t\t\t {quantidade_p[lipe]} \t\t\t\t {descricao_p[lipe]}')

def excluir_produtos():
    inf = int(input('Qual deseja excluir: '))
    if inf == inf:
        nome_p.pop(inf), quantidade_p.pop(inf), descricao_p.pop(inf), valor_p.pop(inf)

while True:
    clear()
    print("[1] - Para adicionar um produto")
    print("[2] - Para mostrar produtos")
    print("[3] - Para excuir um produto")
    print("[4] - Para sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        adicionar_produtos()
    elif opcao == 2:
        mostrar_produtos()
    elif opcao == 3:
        excluir_produtos()
    elif opcao == 4:
        break
    inf = str(input('Tecle enter para continuar...'))




