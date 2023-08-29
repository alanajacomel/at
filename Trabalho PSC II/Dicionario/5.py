cidade_populacao = {'São Paulo': 12106920, 'Rio de Janeiro': 6718903, 'Curitiba': 1773733, 'Florianópolis': 537213, 'Foz do Iguaçu ': 285415}

cidade_com_maior_populacao = max(cidade_populacao, key=cidade_populacao.get)

print('Cidade que tem maior númeor de habitante é', cidade_com_maior_populacao)