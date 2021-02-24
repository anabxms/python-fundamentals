# declaração de variáveis
usuarios = {}
maior_media = 0
menor_media = 0
nome_maior_media = ''
nome_menor_media = ''

# adição de valores no dicionário
for i in range(4):
    nome = input(f'Digite o nome do {i+1}º usuário: ')
    foto1 = int(input(f'Digite as curtidas da última foto de {nome.title()}: '))
    foto2 = int(input(f'Digite as curtidas da penúltima foto de {nome.title()}: '))
    foto3 = int(input(f'Digite as curtidas da antepenúltima foto de {nome.title()}: '))
    usuarios[nome] = {foto1, foto2, foto3}

# cálculo da média e do número de maior e menor curtidas
for nome, curtidas in usuarios.items():
    media = sum(curtidas)/len(curtidas)
    if maior_media == 0:
        maior_media = media
        menor_media = media
        nome_maior_media = nome
        nome_menor_media = nome
    else:
        if media > maior_media:
            maior_media = media
            nome_maior_media = nome
        elif media < menor_media:
            menor_media = media
            nome_menor_media = nome
    # resultados
    print(f'{nome.title()}: {media}')
print(f'{nome_maior_media.title()} teve o maior número de curtidas.')
print(f'{nome_menor_media.title()} teve o menor número de curtidas.')
