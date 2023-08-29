nota = set([8, 7, 9, 6])

medias = sum(nota) / len(nota)

if medias >= 7:
    print('Aluno aprovado com média ', medias)
else:
    print('Aluno reprovado com média', medias)