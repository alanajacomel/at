alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

vogal = ('a', 'e', 'i', 'o', 'u')

diferenca = tuple(set(alfabeto).difference(vogal))

print('A diferença entre as duas é:',diferenca)