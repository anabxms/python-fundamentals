# declaração de variáveis
idades = []
acima_media = 0
abaixo_25 = 0
# adição de valores na lista
print('Adicione o valor da idade e, se quiser encerrar, digite um valor igual ou menor que 0:')
while True:
    num = int(input())
    if num <= 0:
        break
    else:
        idades.append(num)
# cálculo de qtd de valores acima da média e abaixo de 25
for idade in idades:
    if idade > sum(idades)/len(idades):
        acima_media += 1
    elif idade < 25:
        abaixo_25 += 1
# impressão dos resultados
print(f'Quantidade de idades válidas: {len(idades)}')
print(f'Soma das idades: {sum(idades)}')
print(f'Média das idades: {sum(idades)/len(idades)}')
print(f'Quant. de idades acima da média: {acima_media}')
print(f'Quant. de idades abaixo de 25: {abaixo_25}')
print('Programa encerrado')
