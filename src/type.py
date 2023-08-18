
# Declaração de Variãveis 
# declaração de variaveis não pode começar com numeros
# 1a = 1 - ERROR

# type Interger: 'int'
int = 10

# type Float: 'float'
float = 0.1

# type String: 'str'
str1 = 'texto'

# type Lista: 'list'
list = ['item1', 'item-2', 'item 3']

# type Tuplas: 'tuple'
# Similar a Lista
tuple = ('item1', 'item-2', 'item 3')

# type Dicionario: 'dict'
dict = { 'nome' : 'fulano', 'idade' : 18}


# EXIBIR Tipologia 
print(type(int))
print(type(float))
print(type(str1))
print(type(list))
print(type(tuple))
print(type(dict))


# Atribuições e operadores
# Atribuição composta 
# a = 10
# b = 0
a, b = 10,0
# Funciona com operaççoes tbm
# resultA = operação e ResultB = Operação
resultA, resultB = a+b,a+a
print('ResultA: ' +str(resultA))
print('ResultB: ' +str(resultB))

# Operadores
resultA += a # soma 10 no valor do resultA
resultB -= b # subtair 0 no valor do resultB
resultA *= a # Muiltiplicar Pelo valor em A
resultA /= a # Dividir pelo valor em A
resultB %= a # Resulto da divisão pelo em A 
print('ResultA Depois: ' +str(resultA))

# Estrutura While
count = 0
print('BEGIN WHILE')
while count < 10:
    # Pular Exibir numero 5 
    if(count ==5):
        print('PULAR')
        count=count+1
        continue
    print(count)
    count=count+1
    #Para no 8 - break = Não roda Else do While
    if(count ==8):
        print('BREAK OUT END')
        break
else:
    print('END WHILE')
    
# Estrutura do FOR 
# For funciona parecido comm forech no JS
# Pega elemento de uma estrutura de list/dict/tuple
print('BEGIN FOR')
for i in [1,2,3]:
    print(i)
else:
    print('END FOR')
    
print('FOR ZIP')   
for i,j in zip([1,2,3],['a', 'b', 'c']):
    print(i, j)
    
print('FOR ENUM')   
for i,j in enumerate(['a', 'b', 'c']):
    print(i, j)
    
    