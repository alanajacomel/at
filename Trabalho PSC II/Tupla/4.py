nomes = ('Edegard', 'Alana', 'Noah', 'Tika', 'Floriano')

numeros = int(input('Escreva um numero de 1 a 5: '))

if 1 <= numeros <= 5:
    nome = nomes[numeros - 1]
    print('Nome correspondente é', nome)
else:
    print('Inválido')