cores = ('Vermelho', 'Laranja', 'Amarelo', 'Verde', 'Azul', 'Anil', 'Violeta')

cor = input('Escreva alguma cor: ')

if cor in cores:
    print('Cor', cor, 'existe no arco-íris')
else:
    print('Cor', cor, 'não existe no arco-íris')
