from calc import soma

if __name__ == '__main__':
    try:
        # testando direto pelo codigo 
        print(soma(5,5))
        print(soma(5.5,5))
        print(soma(-5,5))
        print(soma(-5,'5'))
    except AssertionError as e:
        print(f'Error: Falha na conta - {e}')