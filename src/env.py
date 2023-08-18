import os

# Por segurança converte o valor da variavel em inteiro depois em boolean
DEBUG = bool(int(os.getenv('DEBUG',0)))