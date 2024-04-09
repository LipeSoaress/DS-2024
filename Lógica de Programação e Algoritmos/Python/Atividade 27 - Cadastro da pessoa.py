from click import clear

def adicionar_pessoa():
    nome = input('Digite seu nome: ')
    email = input('Digite seu e-mail: ')

    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}, {email}\n')

    print('Pessoas cadastradas com sucesso!!')

def listar_pessoa():
    with open('pessoas.txt', 'r') as arquivo:
        print('pessoas cadastradas:')
        for linha in arquivo:
            nome, email = linha.strip().split(',')
            print(f'Nome: {nome}, E-mail: {email}\n')

listar_pessoa()
