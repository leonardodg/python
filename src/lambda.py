# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

lista = [4, 32, 1, 34, 5, 6, 6, 21, ] 
lista.sort(reverse=True) # ordernar reverse 
sorted(lista) # ordena a lista com funcção


lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# Função definida para ser utilizada pelo metodo sort
def orderna(item):
    return item['nome']

lista.sort(key=orderna) # ordernar usando function 
lista.sort(key=lambda item: item['nome']) # ordernar usando lambda - faz mesma coisa que a linha anterior sem precisar definir uma função 


# Função apenas para imprimir na tela
def exibir(lista):
    for item in lista:
        print(item)
    print()

# Exemplos criando nova lista
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)