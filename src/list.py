lista = [1,2,3]

el_del = lista.pop() # delete utlimo elemento e retorna o valor
lista.append("adicionar") # adiciona na ultima posição
lista.pop(0) # remover o primeiro elemento
lista.append(10) # adiciona 
print(lista) # imprimir

del lista[-1] # apagar um indice

lista.insert(0, "inicio")
print(lista) # imprimir

lista.clear()
print(lista) # imprimir

lista_a = [1,2,3]
lista_b = [4,5,6]

# união de lista 
lista_c = lista_a + lista_b
# outra forma de união usando metodo e mechendo na lista em questão
lista_a.extend(lista_b)

print(lista_c) # imprimir
print(lista_a) # imprimir


lista_d = lista_a # copia o apontamento na memoria
lista_e = lista_a.copy() # faz uma copia simples dos valores imutaveis 


# Desempacotamento de lista
nomes = ['luiz', 'maria', 'frida', 'helena']

nome1, nome2, nome3, nome4 = nomes # desta forma numero de variaveis precisa ser igual a qtd de elementos da lista

print(nome2) # imprimir
# pegar valores sem o mesmo numeros da variaveis 
# _ underline é uma convesão que o valor será descartado
# *_ returno o resto da lista sem precisar de todas as variaveis 
_, nome, *resto = nomes
_, nome, *_ = nomes

print(nome) # imprimir

# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')


# Tuples é uma lista imutavel
tupla = 'nome1',1, 1.1
tupla1 = ( 'nome1', 'nome2', 'nome3')

print(tupla) # imprimir

tupla3 = tuple(lista)


# Enumerate - interavel de uma lista
# obter o indeces de uma lista
lista = list(tupla)
for item in lista:
    print(item) # print apenas valores

for item in enumerate(lista):
    index, value = item
    print(item, index, value) # print tupla com index, valor

for index, value in enumerate(lista):
    print(index, value) # print tupla com index, valor

lista_enumerada = list(enumerate(lista))
#[(0, 'nome1'), (1, 1), (2, 1.1)]
print(lista_enumerada) # imprimir lista_enumerada


"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável
iteratador = iter(texto)  # iterator

# fazer mesma função do for com iteratador
while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

# exemplo acima
for letra in texto:
    print(letra)

