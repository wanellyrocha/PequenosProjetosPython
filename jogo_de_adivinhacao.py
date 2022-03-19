# Jogo de Adivinhação

import time

secreto = 'boletos'
digitadas = []
chances = 3

print('Duvido vc descobrir a palavra que pensei aqui..')
time.sleep(0.5)
print('Vc tem 3 chances')
time.sleep(0.5)

while True:
    if chances <= 0:    # validador das tentativas
        print('PERDEU!!')
        break

    letra = input('Digite uma letra: ')

    # testando se foi inserido mais de 1 caracter
    if len(letra) > 1:
        print('Nada de migué! É para digitar apenas 01 letra.')
        chances -= 1
        print(f'Vc ainda tem {chances} chance(s).')
        print()
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Aêêê... a letra "{letra}" existe na palavra secreta!')
    else:
        print(f'Xiii... a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()     # retira o último elemento digitado para não armazenar

    # montando como as palavras acertadas aparecerão para o usuário [as dicas]
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Show! Vc ACERTOU!! A palavra secreta era {secreto_temporario}.')
        break
    else:
        print(f'O que temos até agora: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Vc ainda tem {chances} chance(s).')
    print()


