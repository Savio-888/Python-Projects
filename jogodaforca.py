# Faça um programa que funciona como um jogo da forca, onde o usuário digita um número, e o computador acessa uma lista de palavras com o index do número digitado.
# Depois, o usuário tem que adivinhar as letras que a palavra contém, com 6 chances para erro.

tupla = ('BANANA', 'BOLA', 'PEDRA', 'ARPÃO', 'LIVRO', 'COLCHÃO')

while True:
    i = int(input('Digite um número de 1 a 6\n>> '))
    palavra = tupla[i]
    certo = set()
    chance = 5
    while certo != set(palavra): # Checa se a palavra ainda não foi descoberta, usando a variável de classe set 'certo', e a comparando com a string 'palavra'.
        for c in range(0, len(palavra)): # Exibe as letras já descobertas, além do número de letras da palavra.
            if palavra[c] in certo:
                print(f'{palavra[c]}', end='')
            else:
                print('_', end='')
        print(f'\n{len(palavra)} LETRAS.\n{chance} CHANCES.')
        letra = input('\nDigite uma letra:\n>> ').upper() # Pede uma letra para o usuário.
        while len(letra) != 1 and letra.isalpha() is False: # Caso o valor inserido seja maior que duas letras, ou simplesmente não seja uma letra:
            letra = input('\nERRO: Letra invalida. Digite novamente:\n>> ')
        if letra in set(palavra): # Checa se a letra está presente na palavra, independente da posição.
            certo.add(letra)
        else: # ...Se não estiver, o usuário perde uma chance
            chance -= 1
            if chance == 0: # Se chegar a 0, o usuário perde
                break
    print(palavra)
    if chance == 0: # Checando se o usuário acertou ou não.
        print('Você não conseguiu acertar a palavra...')
    else:
        print('PARABENS! Você acertou a palavra!')
    escolha = input('Gostaria de reiniciar? [S/N]\n>> ') # Decide se o programa continua ou termina
    if escolha in 'sSnN': # Checa o valor inserido, continuando o loop, ou saindo dele e terminando o programa.
        if escolha in 'sS':
            continue
        else:
            break
    else: # Caso o valor inserido na escolha não seja válido:
        while escolha not in 'sSnN':
            escolha = input('ERRO: Digite novamente a escolha [S/N]\n>> ')
