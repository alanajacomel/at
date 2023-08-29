estado_capital = {'Paraná': 'Curitiba', 'Santa Catarina': 'Florianoplis', 'Minas Gerais': 'Belo Horizonte'}

estado = input('Esecreva um estado:  ')
capital = estado_capital.get(estado)
if capital:
    print('Capital de', estado, 'é', capital)
else:
    print('Estado não encontrado')