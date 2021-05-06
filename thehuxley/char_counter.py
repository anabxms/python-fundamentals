# Escreva um programa que receba um texto em uma única linha e imprima cada caractere e o
# número de vezes que ocorre no texto, na ordem inversa à alfabética.

# Formato de entrada
# Uma linha contendo qualquer caractere, que pode incluir letras, números, pontuação e
# caracteres especiais.

# Formato de saída
# Uma sequência linhas onde cada linha contém um caractere e seu respectivo número de
# ocorrências no texto. A sequência de caracteres segue a ordem alfabética decrescente.

palavra = input()

letras = {}

for letra in palavra:
    if letra not in letras.keys():
        letras[letra] = palavra.count(letra)

for letra in sorted(letras, reverse=True):
    print(f"{letra} {letras[letra]}")
