"""
lista = []

lista.append('v1')
lista.append('v2')
lista.append('v3')

print(lista)
----------------------------------------------------
frutas = []
frutas.append('Maçã')
frutas.append('Bergamota')
frutas.append('Banana')
frutas.append('Melão')
frutas.append('Laranja')
print(frutas)
print(len(frutas))
frutas.pop(0)
print(frutas)
frutas.pop(-1)
print(len(frutas))
print(frutas)
print(len(frutas[0]))
frutas.clear()
print(frutas)
#print(f"Lista de frutas: {frutas[0]} e {frutas[2]}")
----------------------------------------------------
tarefas = []

for i in range(0, 10):
    tarefa = input(f'Digite a sua tarefa número {i+1}: ')
    tarefas.append(tarefa)
print(tarefas)
----------------------------------------------------
tarefas = []
contador = 0
while contador < 10:
    tarefa = input(f'Digite a sua tarefa número {contador+1}: ')
    tarefas.append(tarefa)
    contador += 1
print(tarefas)
----------------------------------------------------
lista = []

lista.append(1)
lista.append('jorge')
lista.append(33.7)
lista.append(True)
print(type(lista))
print(type(lista[0]))
print(type(lista[1]))
print(type(lista[2]))
print(type(lista[3]))
---------------------------------------------------
"""