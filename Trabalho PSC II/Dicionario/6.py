alimento_calorias = {'Maçã': 52, 'Morango': 45, 'Pão francês': 150}

alimento = input('Esecreva um alimento: ')

calorias = alimento_calorias.get(alimento)

if calorias:
    print('Alimento', alimento, 'tem o total de', calorias, 'calorias')
else:
    print('Alimento não encontrado')