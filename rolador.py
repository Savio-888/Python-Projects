# Rolador de dados, com multiplas opções de modos para rolar

from random import randint # Importando função utilizazdo para rolar o dado
import os # Importa os comandos do sistema operacional
import time # Importa os comandos de tempo
while True: # Loop
    try: # Pegando Inputs do usuário
        numd = int(input('Digite o número de dados:\n>> '))
        while numd < 0: # Caso valor negativo seja digitado.
            numd = int(input('ERRO: Valor digitado é invalido (número de dados não pode ser negativo).\nDigite novamente:\n>>'))
        lados = int(input('Digite o número de lados do dado:\n>> '))
        while lados < 0: # Caso valor negativo seja digitado.
            lados = int(input('ERRO: Valor digitado é invalido (número de lados não pode ser negativo).\nDigite novamente:\n>>'))
        mod = int(input('Digite o Modificador do teste (se não houver, digitar 0.)\n>> '))
        modo = input('Digite o Modo (Vantagem[V]/Desvantagem[D]/Normal[N]):\n>> ').upper()
        while modo not in 'VDN': # Caso o modo digitado seja inválido.
            modo = input('ERRO: Modo digitado é inválido.\nDigite o Modo novamente (Vantagem[V]/Desvantagem[D]/Normal[N]):\n>> ').upper()
    except ValueError: # caso o valor digitado não seja válido
        print("ERRO: Valor Inválido digitado, Reiniciando...")
        time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue # Recomeça o Loop
    
    rolagens = list() # Cria a váriavel rolagens para armazenar as rolagens dos dados

    match modo: # Verifica o modo digitado
        case 'N': # Rola todos os dados e os soma com o modificador no final
            for i in range(0, numd):
                rolagens.append(randint(1, lados))
            print(f'Os rolagens foram {rolagens}, a soma deles foi de {sum(rolagens)+mod} (', end='')
            for i in range(0, numd):
                print(f'{rolagens[i]}+', end='')
            print(f'{mod})')
        case 'V': # Rola todos os dados e soma somente o maior com o modificador no final
            for i in range(0, numd):
                rolagens.append(randint(1, lados))
            rolagens.sort() # organiza as rolagens em ordem crescente
            print(f'O resultado {rolagens[-1]+mod} ({rolagens[-1]}+{mod}) ({rolagens})')
        case 'D': # Rola todos os dados e soma somente o menor com o modificador no final
            for i in range(0, numd):
                rolagens.append(randint(1, lados))
            rolagens.sort() # organiza as rolagens em ordem crescente
            print(f'O resultado {rolagens[0]+mod} ({rolagens[0]}+{mod}) ({rolagens})')
    
    escolha = input('Deseja continuar rolando? [N/S]\n>> ').upper()
    while escolha not in 'NS':
        escolha = input('ERRO: Valor inválido digitado.\nDeseja continuar rolando? [N/S]\n>> ').upper()
    if escolha in 'S': # Continua no loop
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    os.system('cls' if os.name == 'nt' else 'clear')
    break # Termina o loop
