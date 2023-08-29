jogo_jogador = {'Futebol': 22, 'Vôlei': 12, 'Basquete': 10}

jogo = input('Esecrva nome de algum jogo: ')
jogadores = jogo_jogador.get(jogo)

if jogadores:
    print('O', jogo, 'precisa de', jogadores, 'jogadores')
else:
    print('Jogo não existe')