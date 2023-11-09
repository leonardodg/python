def soma(x,y):
    """"
        Função Soma: Somar dois numeros X e Y

        > Exemplo de como executar a função soma no DocString com Doctest

        - Com sinais de maior >>> executa a função - exemplo
        >>> soma(10,20)
        30

        - exemplo de teste que passou com returno da exceção esperado
        >>> soma(10, '20')
        Traceback (most recent call last):
        ...
        AssertionError: y precisa ser int ou float
    """

    # assert funciona igual levantar uma excet com raise porem já faz a condição junto
    assert isinstance(x, (int , float)), 'x precisa ser int ou float'
    assert isinstance(y, (int , float)), 'y precisa ser int ou float'
    return x + y


# Apenas para executar o teste quando modulo for executado diretamente
if __name__ == '__main__': 
    import doctest
    doctest.testmod(verbose=True) # verbose mostra os resultado

