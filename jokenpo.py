import os 
import random
jogadas1 = 0
jogadas2 = 0

print('Bem vindo(a) ao jogo do pedra, papel e tesoura')
print('Você terá três opções de jogo: \n1. Jogador x Jogador \n2. Jogador x Computador \n3. Computador x Computador \n4.Sair')
opcoes = int(input('Qual você deseja jogar? '))
os.system('clear')

while opcoes != 1 and opcoes != 2 and opcoes != 3 and opcoes != 4:
    print('Eiii! Essa opção não existe!')
    print('\nVocê terá três opções de jogo: \n1. Jogador x Jogador \n2. Jogador x Computador \n3. Computador x Computador \n4.Sair')
    opcoes = int(input('Qual você deseja jogar? '))
    os.system('clear')

if opcoes == 1:
    nomeJogador1 = input('Jogador 1, digite seu nome: ').capitalize()
    nomeJogador2 = input('Jogador 2, digite seu nome: ').capitalize()
    resposta1 = 1

    while resposta1 == 1:
        jogada1 = input(f'\n{nomeJogador1}, faça sua jogada (pedra, papel ou tesoura): ').lower()
        os.system('clear')
        jogada2 = input(f'\n{nomeJogador2}, faça sua jogada (pedra, papel ou tesoura): ').lower()
        os.system('clear')

        if jogada1 == 'tesoura' and jogada2 == 'pedra' or jogada1 == 'papel' and jogada2 == 'tesoura' or jogada1 == 'pedra' and jogada2 == 'papel':
            resposta1 = int(input(f'{nomeJogador2} venceu! Desejam jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas2 += 1           
        elif jogada1 == 'pedra' and jogada2 == 'tesoura' or jogada1 == 'tesoura' and jogada2 == 'papel' or jogada1 == 'papel' and jogada2 == 'pedra':
            resposta1 = int(input(f'{nomeJogador1} venceu! Desejam jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas1 += 1
        elif jogada1 == 'pedra' and jogada2 == 'pedra' or jogada1 == 'tesoura' and jogada2 == 'tesoura' or jogada1 == 'papel' and jogada2 == 'papel': 
            resposta1 = int(input(f'{nomeJogador1} e {nomeJogador2} empataram! Desejam jogar novamente?\n(Digite 1 para Sim e 2 para Não): '))  
        else:
            resposta1 = int(input(f'Ei, essa jogada não existe! Desejam jogar novamente?\n(Digite 1 para Sim e 2 para Não): ')) 

    if jogadas1 > jogadas2:
        print(f'\nParabéns {nomeJogador1}, você foi o(a) vencedor(a)! \nPlacar final: {nomeJogador1} {jogadas1} x {jogadas2} {nomeJogador2}')
        print('Muito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
    elif jogadas1 < jogadas2:
        print(f'\nParabéns {nomeJogador2}, você foi o(a) vencedor(a)! \nPlacar final: {nomeJogador2} {jogadas2} x {jogadas1} {nomeJogador1}')
        print('Muito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
    else:
        print(f'\nHouve um empate! \nPlacar final: {nomeJogador1} {jogadas1} x {jogadas2} {nomeJogador2}')
            
elif opcoes == 2:
    nomeJogador = input('Digite seu nome: ').capitalize()
    resposta1 = 1

    while resposta1 == 1:
        jogada1 = input(f'\nFaça sua jogada (pedra, papel ou tesoura): ').lower()
        jogadaBotAleatoria = random.randint(1,3) 
        if jogadaBotAleatoria == 1:
            jogadaBot = 'pedra'
        elif jogadaBotAleatoria == 2:
            jogadaBot = 'papel'
        else:
            jogadaBot = 'tesoura'
        print(f'O computador jogou {jogadaBot}')
        if jogada1 != 'tesoura' and jogada1 != 'papel'and jogada1 != 'pedra':
            resposta1 = int(input(f'\nEi, essa jogada não existe! Desejam jogar novamente?\n(Digite 1 para Sim e 2 para Não): '))
        elif jogada1 == 'tesoura' and jogadaBot == 'pedra' or jogada1 == 'papel' and jogadaBot == 'tesoura' or jogada1 == 'pedra' and jogadaBot == 'papel':
            resposta1 = int(input(f'\nComputador venceu! Deseja jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas2 += 1
        elif jogada1 == 'pedra' and jogadaBot == 'tesoura' or jogada1 == 'tesoura' and jogadaBot == 'papel' or jogada1 == 'papel' and jogadaBot == 'pedra':
            resposta1 = int(input(f'\nVocê venceu! Deseja jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas1 += 1
        elif jogada1 == 'pedra' and jogadaBot == 'pedra' or jogada1 == 'tesoura' and jogadaBot == 'tesoura' or jogada1 == 'papel' and jogadaBot == 'papel': 
            resposta1 = int(input(f'{nomeJogador} e computador empataram! Deseja jogar novamente?\n(Digite 1 para Sim e 2 para Não): '))
             
    if jogadas1 > jogadas2:
        print(f'\nParabéns {nomeJogador}, você foi o(a) vencedor(a)! \nPlacar final: {nomeJogador} {jogadas1} x {jogadas2} Computador')
        print('Muito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
    elif jogadas1 < jogadas2:
        print(f'\nO computador foi o vencedor! \nPlacar final: Computador {jogadas2} x {jogadas1} {nomeJogador}')
        print('Muito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
    else:
        print(f'\nHouve um empate! \nPlacar final: {nomeJogador} {jogadas1} x {jogadas2} Computador')

elif opcoes == 3:
    resposta1 = 1

    while resposta1 == 1:
        jogadaBotAleatoria1 = random.randint(1,3)
        if jogadaBotAleatoria1 == 1:
            jogadaBot1 = 'pedra'
        elif jogadaBotAleatoria1 == 2:
            jogadaBot1 = 'papel'
        else:
            jogadaBot1 = 'tesoura'
        jogadaBotAleatoria2 = random.randint(1,3)
        if jogadaBotAleatoria2 == 1:
            jogadaBot2 = 'pedra'
        elif jogadaBotAleatoria2 == 2:
            jogadaBot2 = 'papel'
        else:
            jogadaBot2 = 'tesoura'
        print(f'\nO computador 1 jogou {jogadaBot1} \nO computador 2 jogou {jogadaBot2}')
        if jogadaBot1 == 'tesoura' and jogadaBot2 == 'pedra' or jogadaBot1 == 'papel' and jogadaBot2 == 'tesoura' or jogadaBot1 == 'pedra' and jogadaBot2 == 'papel':
            resposta1 = int(input('\nComputador 2 venceu! Deseja jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas2 += 1
        elif jogadaBot2 == 'tesoura' and jogadaBot1 == 'pedra' or jogadaBot1 == 'papel' and jogadaBot2 == 'tesoura' or jogadaBot1 == 'pedra' and jogadaBot2 == 'papel':
            resposta1 = int(input('\nComputador 1 venceu! Deseja jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas1 += 1
        else: 
            resposta1 = int(input('\nComputador 1 e computador 2 empataram! Deseja jogar novamente?\n(Digite 1 para Sim e 2 para Não): '))     
    if jogadas1 > jogadas2:
        print(f'\nO computador 1 venceu! \nPlacar final: Computador 1 {jogadas1} x {jogadas2} Computador 2')
        print('Muito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
    elif jogadas1 < jogadas2:
        print(f'\nO computador 2 foi o vencedor! \nPlacar final: Computador 2 {jogadas2} x {jogadas1} Computador 1')
        print('Muito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
    else:
        print(f'\nHouve um empate! \nPlacar final: Computador 1 {jogadas1} x {jogadas2} Computador 2')

elif opcoes == 4:
    print('\nJá vai? Obrigada por participar do jogo! \nFernanda Rodrigues, Isabela Louise e Julia Molina')
