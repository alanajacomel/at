primos = set([2, 3, 5, 7, 11, 13, 17, 19])

numeros = int(input('Escreva algum número: '))

if numeros in primos:
    print('Número', numeros, 'é primo e existe no conjunto')
else:
    print('Número', numeros, 'não é primo ou não existe no conjunto')