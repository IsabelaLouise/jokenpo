#importar o sistema para limpar o terminal e randomizar a escolha do computador
import os 
import random

#iniciar o contador das jogadas
jogadas1 = 0
jogadas2 = 0

#introdução para o jogo e pergunta qual numero o usuario quer
print('\nBem vindo(a) ao jogo do pedra, papel e tesoura!')
print('\nVocê terá três opções de jogo: \n1. Jogador x Jogador \n2. Jogador x Computador \n3. Computador x Computador \n4. Sair')
opcoes = int(input('\nQual você deseja jogar? '))
os.system('clear')

#configuração para que se op numero digitado não for 1, 2, 3 ou 4 aparece o recado que não existe e repete as opções
while opcoes != 1 and opcoes != 2 and opcoes != 3 and opcoes != 4:
    print('Eiii! Essa opção não existe!')
    print('\nVocê terá três opções de jogo: \n1. Jogador x Jogador \n2. Jogador x Computador \n3. Computador x Computador \n4.Sair')
    opcoes = int(input('\nQual você deseja jogar? '))
    os.system('clear')

#----------------------------------------------------------------------------------------------------------

#se o usuario digitar um (jogador x jogador) ele pede o nome dos dois jogadores
if opcoes == 1:
    nomeJogador1 = input('\nJogador 1, digite seu nome: ').capitalize()
    nomeJogador2 = input('\nJogador 2, digite seu nome: ').capitalize()
    resposta1 = 1
#como a variavel da resposta1 foi criada, deixamos em 1, pois mais abaixo vamos pedir nessa variavel se ele quer continuar digite 1, entao enquanto o 1 acontecer isso vai repetir 
    while resposta1 == 1:
        jogada1 = input(f'\n{nomeJogador1}, faça sua jogada (pedra, papel ou tesoura): ').lower()
        os.system('clear')
        jogada2 = input(f'\n{nomeJogador2}, faça sua jogada (pedra, papel ou tesoura): ').lower()
        os.system('clear')

#fizemos todas as possibilidades que o jogador 2 ganhara, logo emitira a mensagem que o jogador 2 ganhou e adicionar a contagem do jogador 2
        if jogada1 == 'tesoura' and jogada2 == 'pedra' or jogada1 == 'papel' and jogada2 == 'tesoura' or jogada1 == 'pedra' and jogada2 == 'papel':
            resposta1 = int(input(f'\n{nomeJogador2} venceu! Desejam jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas2 += 1   
#fizemos todas as possibilidades que o jogador 1 ganhara, logo emitira a mensagem que o jogador 1 ganhou e adicionar a contagem do jogador 1        
        elif jogada1 == 'pedra' and jogada2 == 'tesoura' or jogada1 == 'tesoura' and jogada2 == 'papel' or jogada1 == 'papel' and jogada2 == 'pedra':
            resposta1 = int(input(f'\n{nomeJogador1} venceu! Desejam jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas1 += 1
#fizemos quando os dois jogarem a mesma coisa, aparecera que empataram
        elif jogada1 == 'pedra' and jogada2 == 'pedra' or jogada1 == 'tesoura' and jogada2 == 'tesoura' or jogada1 == 'papel' and jogada2 == 'papel': 
            resposta1 = int(input(f'\n{nomeJogador1} e {nomeJogador2} empataram! Desejam jogar novamente?\n(Digite 1 para Sim e 2 para Não): '))  
#se os usuarios digitarem qualquer outra coisa vai aparecer que nao existe a possibilidade e se querem continuar jogando
        else:
            resposta1 = int(input(f'\nEi, essa jogada não existe! Desejam jogar novamente?\n(Digite 1 para Sim e 2 para Não): ')) 

#agora que esta fora do while, considerando que o usuario digitou 2, para sair e consideramos se a jogada do jogador1 for maior que do dois, então a gente parabeniza o jogador 1 e finaliza o jogo
    if jogadas1 > jogadas2:
        print(f'\nParabéns {nomeJogador1}, você foi o(a) vencedor(a)! \nPlacar final: {nomeJogador1} {jogadas1} x {jogadas2} {nomeJogador2}')
        print('\nMuito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
#mesma coisa para se o jogador 2 tiver mais vitorias que o 1
    elif jogadas1 < jogadas2:
        print(f'\nParabéns {nomeJogador2}, você foi o(a) vencedor(a)! \nPlacar final: {nomeJogador2} {jogadas2} x {jogadas1} {nomeJogador1}')
        print('\nMuito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
#agora oque sobrou é se empatar, então mostra mensagem de empate
    else:
        print(f'\nHouve um empate! \nPlacar final: {nomeJogador1} {jogadas1} x {jogadas2} {nomeJogador2}')
        print('\nMuito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
        
#---------------------------------------------------------------------------------------------------------

#agora se o usuario escolher jogador x computador, oedimos o nome do usuario
elif opcoes == 2:
    nomeJogador = input('Digite seu nome: ').capitalize()
    resposta1 = 1

#mesma coisa da outra possibilidade, a resposta é para se deseja continuar e logo pede a jogada do usuario
    while resposta1 == 1:
        jogada1 = input(f'\nFaça sua jogada (pedra, papel ou tesoura): ').lower()
#jogada do bot com randity e a possibilidade de 1 valer pedra, 2 valer papel e 3 valer tesoura e depois mostrar pro usuario qual foi a jogada do computador
        jogadaBotAleatoria = random.randint(1,3) 
        if jogadaBotAleatoria == 1:
            jogadaBot = 'pedra'
        elif jogadaBotAleatoria == 2:
            jogadaBot = 'papel'
        else:
            jogadaBot = 'tesoura'
        print(f'\nO computador jogou {jogadaBot}')
#fizemos a possibilidade da jogada for diferente doque pedimos, entao informamos que nao existe e perguntamos se quer jogar denovo
        if jogada1 != 'tesoura' and jogada1 != 'papel'and jogada1 != 'pedra':
            resposta1 = int(input(f'\nEi, essa jogada não existe! Desejam jogar novamente?\n(Digite 1 para Sim e 2 para Não): '))
#aqui fizemos as possibilidades que o computador vence e informamos isso ao usuario, tambem somando no placar dele
        elif jogada1 == 'tesoura' and jogadaBot == 'pedra' or jogada1 == 'papel' and jogadaBot == 'tesoura' or jogada1 == 'pedra' and jogadaBot == 'papel':
            resposta1 = int(input(f'\nComputador venceu! Deseja jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas2 += 1
#possibilidade de que o usuario vence, entao informamops que o usuario venceu e e perguntamos se uqer jogar denovo
        elif jogada1 == 'pedra' and jogadaBot == 'tesoura' or jogada1 == 'tesoura' and jogadaBot == 'papel' or jogada1 == 'papel' and jogadaBot == 'pedra':
            resposta1 = int(input(f'\nVocê venceu! Deseja jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas1 += 1
#possibilidades de que eles empatem e informamos que foi empate
        elif jogada1 == 'pedra' and jogadaBot == 'pedra' or jogada1 == 'tesoura' and jogadaBot == 'tesoura' or jogada1 == 'papel' and jogadaBot == 'papel': 
            resposta1 = int(input(f'\n{nomeJogador} e computador empataram! Deseja jogar novamente?\n(Digite 1 para Sim e 2 para Não): '))

#aqui esta fora do while, entao o jogador pediu para sair e informamos se o usuario venceu e o placar             
    if jogadas1 > jogadas2:
        print(f'\nParabéns {nomeJogador}, você foi o(a) vencedor(a)! \nPlacar final: {nomeJogador} {jogadas1} x {jogadas2} Computador')
        print('\nMuito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
#mesma coisa, porem se o computador venceu
    elif jogadas1 < jogadas2:
        print(f'\nO computador foi o vencedor! \nPlacar final: Computador {jogadas2} x {jogadas1} {nomeJogador}')
        print('\nMuito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
#e se caso houvesse empate, então informa isso
    else:
        print(f'\nHouve um empate! \nPlacar final: {nomeJogador} {jogadas1} x {jogadas2} Computador')
        print('\nMuito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')

#-----------------------------------------------------------------------------------------------------------

#se o usuario escolher a opcao 3 computador x computador iniciamos uma outra jogada
elif opcoes == 3:
    resposta1 = 1

#colocamos os computadores, assim como fizemos com o computador x usuario para fazer o random e informamos quais foram as jopgadas dos dois computadores 
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
#fizemos as possibilidades do computador 2 vencer, entao informamos que ele ganhou e somamos no contador da jogada dele
        if jogadaBot1 == 'tesoura' and jogadaBot2 == 'pedra' or jogadaBot1 == 'papel' and jogadaBot2 == 'tesoura' or jogadaBot1 == 'pedra' and jogadaBot2 == 'papel':
            resposta1 = int(input('\nComputador 2 venceu! Deseja jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas2 += 1
#fizemos as mesmas possibilidades mas caso o computador 1 vencer
        elif jogadaBot2 == 'tesoura' and jogadaBot1 == 'pedra' or jogadaBot1 == 'papel' and jogadaBot2 == 'tesoura' or jogadaBot1 == 'pedra' and jogadaBot2 == 'papel':
            resposta1 = int(input('\nComputador 1 venceu! Deseja jogar novamente? \n(Digite 1 para Sim e 2 para Não): '))
            jogadas1 += 1
#e caso empatarem informamos isso para o usuario saber
        else: 
            resposta1 = int(input('\nComputador 1 e computador 2 empataram! Deseja jogar novamente?\n(Digite 1 para Sim e 2 para Não): '))     
#caso o usuario selecione 2, sai do while e mostra o placar e se o computador 1 vencer mostra o recado
    if jogadas1 > jogadas2:
        print(f'\nO computador 1 venceu! \nPlacar final: Computador 1 {jogadas1} x {jogadas2} Computador 2')
        print('\nMuito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
#caso o computador 2 vencer aparece a mensagem disso
    elif jogadas1 < jogadas2:
        print(f'\nO computador 2 foi o vencedor! \nPlacar final: Computador 2 {jogadas2} x {jogadas1} Computador 1')
        print('\nMuito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
#caso eles empatem isso tambem é infomado com o placar final
    else:
        print(f'\nHouve um empate! \nPlacar final: Computador 1 {jogadas1} x {jogadas2} Computador 2')
        print('\nMuito obrigada por jogar nosso jogo!\nFernanda Rodrigues, Isabela Louise e Julia Molina')
        
#-----------------------------------------------------------------------------------------------------------

#e se o usuario escolher a opcao 4 que é sair, entao nos despedimos
elif opcoes == 4:
    print('\nJá vai? Obrigada por participar do jogo! \nFernanda Rodrigues, Isabela Louise e Julia Molina')