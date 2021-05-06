# declaração de variáveis
nomes = []
pesos = []
i = 0

# adição de informações nas listas e tupla
while i < 5:
    peso = float(input('Digite o peso: '))
    nome = input('Digite o nome: ')
    if peso >= 50:
        nomes.append(nome)
        pesos.append(peso)
        i += 1
cadastro = (nomes, pesos)

# resultado
print(cadastro)
