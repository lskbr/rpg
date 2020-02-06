# Versao inicial copiada da lista Python Brasil

from random import randint, choice
from time import sleep
from typing import List

# 0001 - f-strings, quebra da validinput
# 0002 - movendo o input para dentro de valida_str e valida_int, type hints


def valida_str(limite, msg) -> str:
    while True:
        valor = input(msg).strip().upper()
        if not valor.isalpha() or valor not in limite or len(valor) == 0:
            print(' OPÇÃO INVÁLIDA !!!\n')
        else:
            break
    return valor


def valida_int(nome: str, limite, mensagem: str) -> int:
    while True:
        valor = input(mensagem).strip()
        if not valor.isnumeric() or valor.isalpha() or len(valor) == 0 or int(valor) not in limite:
            if not valor.isnumeric() or valor.isalpha() or len(valor) == 0:
                print(' OPÇÃO INVÁLIDA !!!\n')
            elif nome == 'inimigo':
                print(' INIMIGO NÃO SE ENCONTRA NA LISTA !!!\n')
            elif nome == 'inimigo_s':
                print(' INIMIGO NÃO SE ENCONTRA NA LISTA !!!\n')
            elif nome == 'ninimigos':
                print(' NÚMERO INVÁLIDO !!!\n')
            else:
                print(' OPÇÃO INVÁLIDA !!!\n')
        else:
            break
    return int(valor)


def instrucao():
    titulo_regra = '.::..::| INSTRUÇÕES/REGRAS |::..::.'
    print(f'\n{titulo_regra:^40}')
    print('\n      - Escolha o número de inimigos;\n\n      '
          '- Escolha a ação desejada;\n\n      - ATACAR:\n\n          '
          'O Herói SEMPRE acerta o inimigo, infligindo 10-15 de dano ao alvo selecionado;\n\n'
          '       - CURAR:\n\n          Recupera 20-50 pontos de vida do Herói, custo de 10 SP;\n\n'
          '       - MODO BESERKER:\n\n               Ao ter seu limite levado ao extremo, o Herói rompe as barreiras \n'
          '               de suas limitações mundanas, elevando-se ao status BESERKER; (Ler REGRA abaixo)\n\n       '
          '- SUPER CURA:\n\n          Recupera 250 pontos de vida do Herói, custo de 50 SP; (Ler REGRA abaixo)\n\n       '
          '- ATAQUE INIMIGO:\n\n          O inimigo terá 25% de chance de errar o ataque (50% após o MODO BESERKER) , caso contrário, \n'
          '          infligirá 1-3 pontos de dano ao Herói; \n\n       REGRA_Geral:\n\n            '
          'A cada rodada você ganhará 3 de SP, a não ser \n            quando o "MODO BESERKER" for DESATIVADO; \n\n       '
          'REGRAS_Beserker: \n\n        - O MODO BESERKER será ativado 1 VEZ por jogo;\n\n        - Contém DUAS RODADAS;\n\n        '
          '- Em cada rodada, o heroi irá realizar ATAQUES SUCESSIVOS e ALEATÓRIOS;\n          '
          '( o jogador não poderá escolher o inimigo a ser atacado neste modo.)\n\n        '
          '- O nº de ataques POR RODADA, será igual à quantidade de inimigo no campo de batalha;\n\n        '
          '- Cada ataque, gera 20-40 pontos de dano ao inimigo;\n\n        - O inimigo não consegue atacar o Herói no MODO BESERKER;\n\n        '
          '- Ao final das duas rodadas, o MODO BESERKER será DESATIVADO;\n\n        '
          '- O Herói irá drenar, em forma de pontos de vida, 10% do DANO TOTAL \n         '
          ' aplicado por ele nas duas rodadas;\n\n        - Ao ser DESATIVADO, o Herói terá ZERO de SP;      '
          '\n\n       REGRA_Super_Cura:\n            '
          'Requisitos para ATIVAR a "SUPER CURA":   \n            - Nº de inimigos > 10;\n            '
          '- Nº de turnos na partida for múltiplo de 10;\n\n      ')
    input('\n\n.::| PRESSIONE ENTER PARA COMEÇAR |::.\n')


titulo = f"{'-' * 40}  A LENDA DO BESERKER {'-' * 40}"
tam_titulo = len(titulo)
print('\n' + '=' * tam_titulo)
print(titulo)
print('=' * tam_titulo)
jogando = False
iniciar = valida_str('CI', '\n Pressione (C)omeçar ou (I)nstruções:\n')

if iniciar == 'C':
    jogando = True

elif iniciar == 'I':
    instrucao()
    jogando = True

while jogando:
    player_vida = 250
    player_sp = 100
    inimigo_vida = 50
    n_rodadas_antes_b = 0
    n_rodadas = 0
    n_rodadas_b = 0
    n_super_cura = True
    n_inimigos = valida_int("ninimigos", range(1, 50), '\n Escolha o número de inimigos:\n')

    lista_inimigo: List[List[int]] = []

    for i in range(n_inimigos):
        lista_inimigo.append([i + 1, inimigo_vida])

    while True:
        if n_rodadas_b == 2:
            n_rodadas_b = 3
        print('\n-----.::| LISTA DE INIMIGOS |::.-----\n')
        sleep(1.5)
        for numero, vida in lista_inimigo:
            print(f' - inimigo ({numero}) -- vida = {vida}')
            if n_inimigos <= 20:
                sleep(0.25)
            elif n_inimigos <= 50:
                sleep(0.1)

        print('\n Nº de inimigos = {}'.format(n_inimigos))
        print('\n\n=====' + ' STATUS DO HERÓI ' + '=====')
        if n_rodadas_b == 3:
            if n_rodadas % 10 == 0:
                if player_sp < 25:
                    player_sp += 72
                    print('\n HERÓI GANHOU 75 SP !!!')
                    sleep(2)
        print('\n  VIDA = {}'.format(player_vida))
        print('  SP = {}\n'.format(player_sp))
        print('-----' + '.::| TURNO DO HERÓI |::.' + '-----' + '\n')
        sleep(1.5)
        erro_skill = True
        while erro_skill:
            if n_rodadas > 0:
                if n_inimigos > 10 and n_rodadas % 10 == 0:
                    print('-----' + '.::| SUPER-CURA ativada |::.' + '-----' + '\n')
            opcao = valida_int('opcao', [1, 2], ' Selecione ATACAR (1), SKIlls (2): \n')
            if opcao == 1:
                erro_skill = False
                lista_limite = []
                for inimigo in lista_inimigo:
                    lista_limite.append(inimigo[0])

                inimigo = valida_int('inimigo', lista_limite, ' Selecione um inimigo da lista acima: \n')
                escolhido = []
                for i in lista_inimigo:
                    if i[0] == int(inimigo):
                        escolhido = i
                        break

                dano_player = randint(15, 20)
                pv_inimigo_antes = escolhido[1]
                escolhido[1] -= dano_player
                print(' Atacando o inimigo {}'.format(escolhido[0]))
                sleep(1.5)
                print(f"\n Você causou {dano_player} de dano ao inimigo {escolhido[0]} ! ({pv_inimigo_antes} - {dano_player} = {escolhido[1]})")
                sleep(1.5)
                if escolhido[1] <= 0:
                    str_inimigo = str(escolhido[0])
                    tam_str_inimigo = len(str_inimigo)
                    msg_morte = '   Voce matou o inimigo {}!'.format(str_inimigo)
                    tam_msg_morte = len(msg_morte)
                    print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1))
                    print(msg_morte)
                    print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1) + '\n')
                    sleep(1.25)
                    lista_inimigo.remove(escolhido)
                    n_inimigos -= 1
            elif opcao == 2:
                erro_skill = False
                while 1:
                    if erro_skill:
                        break
                    if n_rodadas % 10 == 0 and n_rodadas != 0 and n_inimigos > 10:
                        skill = valida_int('skill', [1, 2, 3, 4], ' Selecione a Skill desejada: \n '
                                                                  '- PIERCE (1)\n '
                                                                  '- SLASH (2)\n '
                                                                  '- CURAR (3)\n '
                                                                  '- SUPER-CURA (4)\n')
                    else:
                        skill = valida_int('skill', [1, 2, 3], ' Selecione a Skill desejada: \n '
                                                               '- PIERCE (1)\n '
                                                               '- SLASH (2)\n '
                                                               '- CURAR (3)\n')
                    lista_limite = []
                    for inimigo in lista_inimigo:
                        lista_limite.append(inimigo[0])

                    if skill == 1:
                        if player_sp < 10:
                            print('\n Você não possui SP suficiente (PIERCE = 10 SP)')
                            sleep(3)
                            erro_skill = True
                        else:
                            player_sp -= 10
                            inimigo_p = valida_int('inimigo', lista_limite, ' Selecione um inimigo da lista acima: \n')
                            escolhido = []
                            for i in lista_inimigo:
                                if i[0] == int(inimigo_p):
                                    escolhido = i
                                    break

                            dano_player = randint(25, 40)
                            pv_inimigo_antes = escolhido[1]
                            escolhido[1] -= dano_player
                            print('-' * 30)
                            print(' PIERCE ATTACK no inimigo {}'.format(escolhido[0]))
                            print('-' * 30)
                            sleep(1.5)
                            print(f"\n Você causou {dano_player} de dano ao inimigo {escolhido[0]} ! ({pv_inimigo_antes} - {dano_player} = {escolhido[1]})")
                            sleep(1.5)
                            if escolhido[1] <= 0:
                                str_inimigo = str(escolhido[0])
                                tam_str_inimigo = len(str_inimigo)
                                msg_morte = '   Voce matou o inimigo {}!'.format(str_inimigo)
                                tam_msg_morte = len(msg_morte)
                                print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1))
                                print(msg_morte)
                                print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1) + '\n')
                                sleep(1.25)
                                lista_inimigo.remove(escolhido)
                                n_inimigos -= 1
                            break
                    elif int(skill) == 2:
                        if n_inimigos < 5:
                            print('\n Você não pode usar o SLASH com menos de 5 inimígos')
                            erro_skill = True
                        elif player_sp < 12:
                            print('\n Você não possui SP suficiente (SlASH = 12 SP)')
                            sleep(3)
                            erro_skill = True
                        else:
                            player_sp -= 12
                            cont_slash = 0
                            lista_inimigo_s = []
                            lista_inimigo_s_aux = []
                            opc_skill_2 = valida_int('opc_skill_2', [1, 2],
                                                     ' Selecionar inimigos (1) ou AUTO (2):\n')
                            if opc_skill_2 == 1:
                                while cont_slash < 5:
                                    inimigo_s = valida_int('inimigo', lista_limite, f" Selecione o {cont_slash + 1}º inimigo da lista acima: \n")
                                    lista_inimigo_s_aux.append(inimigo_s)
                                    if lista_inimigo_s_aux.count(inimigo_s) > 1:
                                        print(' INIMIGO REPETIDO !!!\n')
                                        lista_inimigo_s_aux.remove(lista_inimigo_s_aux[(-1)])
                                    else:
                                        cont_slash += 1

                                for i in lista_inimigo_s_aux:
                                    for j in lista_inimigo:
                                        if i == j[0]:
                                            lista_inimigo_s.append(j)

                                pv_inimigo_antes = 0
                                print('--------------------')
                                print(' SLASH ATTACK !!!')
                                print('--------------------')
                                sleep(1.5)
                                for inimigo_s in lista_inimigo_s:
                                    pv_inimigo_antes = inimigo_s[1]
                                    dano_player = randint(20, 35)
                                    inimigo_s[1] -= dano_player
                                    print(f"\n Você causou {dano_player} de dano ao inimigo {inimigo_s[0]} ! ({pv_inimigo_antes} - {dano_player} = {inimigo_s[1]})")
                                    if inimigo_s[1] <= 0:
                                        str_inimigo = str(inimigo_s[0])
                                        tam_str_inimigo = len(str_inimigo)
                                        msg_morte = '   Voce matou o inimigo {}!'.format(str_inimigo)
                                        tam_msg_morte = len(msg_morte)
                                        print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1))
                                        print(msg_morte)
                                        print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1) + '\n')
                                        sleep(1.25)
                                        lista_inimigo.remove(inimigo_s)
                                        n_inimigos -= 1

                                print('\n')
                                sleep(1.5)
                                break
                            elif int(opc_skill_2) == 2:
                                while len(lista_inimigo_s) < 5:
                                    lista_inimigo_s.append(choice(lista_inimigo))
                                    for inimigo_s in lista_inimigo_s:
                                        if lista_inimigo_s.count(inimigo_s) > 1:
                                            lista_inimigo_s.remove(inimigo_s)

                                pv_inimigo_antes = 0
                                print('--------------------')
                                print(' SLASH ATTACK !!!')
                                print('--------------------')
                                sleep(1.5)
                                for inimigo_s in lista_inimigo_s:
                                    pv_inimigo_antes = inimigo_s[1]
                                    dano_player = randint(20, 35)
                                    inimigo_s[1] -= dano_player
                                    print(f"\n Você causou {dano_player} de dano ao inimigo {inimigo_s[0]} ! ({pv_inimigo_antes} - {dano_player} = {inimigo_s[1]})")
                                    if inimigo_s[1] <= 0:
                                        str_inimigo = str(inimigo_s[0])
                                        tam_str_inimigo = len(str_inimigo)
                                        msg_morte = '   Voce matou o inimigo {}!'.format(str_inimigo)
                                        tam_msg_morte = len(msg_morte)
                                        print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1))
                                        print(msg_morte)
                                        print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1) + '\n')
                                        sleep(1.25)
                                        lista_inimigo.remove(inimigo_s)
                                        n_inimigos -= 1

                                sleep(1.5)
                                break
                    elif int(skill) == 3:
                        if player_sp < 8:
                            print('\n Você não possui SP suficiente (CURAR = 8 SP)')
                            sleep(3)
                            erro_skill = True
                        else:
                            cura = randint(30, 50)
                            player_vida += cura
                            player_sp -= 8
                            print(' Você recuperou {} pontos de vida!\n'.format(cura))
                            print('  VIDA: {}'.format(player_vida))
                            print('  SP: {}\n'.format(player_sp))
                            sleep(2)
                            break
                    elif int(skill) == 4:
                        if player_sp < 50:
                            print('\n Você não possui SP suficiente (SUPER CURAR = 50 SP)')
                            sleep(3)
                            erro_skill = True
                        else:
                            player_vida += 250
                            player_sp -= 50
                            n_super_cura = False
                            print(' Você recuperou {} pontos de vida!\n'.format(250))
                            print('  VIDA: {}'.format(player_vida))
                            print('  SP: {}\n'.format(player_sp))
                            sleep(2)
                            break
                    if erro_skill:
                        break

        if n_inimigos == 0:
            sleep(1.5)
            print('\n Nº Inimigos = 0\n')
            print(' .::| PARABÉNS, VOCÊ MATOU TODOS OS INIMIGOS |::.')
            sleep(1)
            restart = valida_str('JS', ' (J)ogar novamente ou (S)air:\n')
            if restart == 'J':
                jogando = True
            elif restart == 'S':
                jogando = False
            break
        soma_dano_inimigo = 0
        print('\n----- .::| TURNO DO INIMIGO |::. -----\n')
        sleep(1.5)
        print('=' * 36)
        for i in lista_inimigo:
            acerto = randint(1, 100)
            if n_rodadas_b == 3:
                if acerto >= 50:
                    dano_inimigo = randint(1, 3)
                    player_vida -= dano_inimigo
                    soma_dano_inimigo += dano_inimigo
                    print('\n Inimigo {} causou {} de dano !'.format(i[0], dano_inimigo))
                    if n_inimigos <= 20:
                        sleep(0.5)
                    elif n_inimigos <= 50:
                        sleep(0.25)
                    else:
                        sleep(0.125)
                else:
                    print('\n Inimigo {} ERROU o ataque!'.format(i[0]))
                    if n_inimigos <= 20:
                        sleep(0.5)
                    elif n_inimigos <= 50:
                        sleep(0.25)
                    else:
                        sleep(0.125)
            else:
                if acerto >= 25:
                    dano_inimigo = randint(1, 3)
                    player_vida -= dano_inimigo
                    soma_dano_inimigo += dano_inimigo
                    print('\n Inimigo {} causou {} de dano !'.format(i[0], dano_inimigo))
                    if n_inimigos <= 20:
                        sleep(0.5)
                    elif n_inimigos <= 50:
                        sleep(0.25)
                    else:
                        sleep(0.125)
                    if player_vida < 0:
                        player_vida = 0
                        dano_b_total_r1 = 0
                        dano_b_total_r2 = 0
                        cont_morte_r1 = 0
                        cont_morte_r2 = 0
                        print('\n VIDA DO HERÓI = {}'.format(player_vida))
                        sleep(3)
                        print(' ...')
                        sleep(1)
                        print(' ..')
                        sleep(1)
                        print(' .')
                        sleep(1)
                        print('\n GOLPE FATAL !!!')
                        sleep(3)
                        print('\n NOSSO HERÓI SUCUMBE DIANTE DA HORDA INIMIGA ...')
                        sleep(5)
                        print(' ...')
                        sleep(1)
                        print(' ..')
                        sleep(1)
                        print(' .')
                        sleep(1)
                        print('\n É O FIM.', end='')
                        sleep(6)
                        print('.', end='')
                        sleep(1)
                        print('.', end='')
                        sleep(1)
                        print(' MAS ESPERE !!!!!\n')
                        sleep(1)
                        print(' O QUE ESTÁ ACONTECENDO...?!?!?\n')
                        sleep(3)
                        print(' NÚVENS NEGRAS SURGEM E O CÉU COMEÇA A ESCURECER...\n')
                        sleep(3)
                        print(' TUDO ESTÁ TREMENDO,\n')
                        sleep(3)
                        print(' RAIOS ECLODEM DA TERRA E RASGAM O CÉU...\n')
                        sleep(3)
                        print(' TROVÕES IRROMPEM TODA A REGIÃO, ESTREMECENDO O ÍMPITO DO INIMIGO.\n')
                        sleep(3)
                        print(' DO MADA, UMA ENORME EXPLOSÃO ARREMESSA OS INIMIGOS CENTENAS DE METROS...\n')
                        sleep(3)
                        print(' DO SEU EPICENTRO, ESTÁ NOSSO HERÓI...\n')
                        sleep(3)
                        print(' MAS AGORA ELE ESTÁ DIFERENTE...\n')
                        sleep(3)
                        print(' AGORA ELE ESTÁ SEDENTO POR SANGUE.\n')
                        sleep(3)
                        print(' NOSSO HERÓI SE TORNOU...UM BESERKER !!!\n')
                        sleep(3)
                        print(' TEMIDO POR SUA IRA, O BESERKER SE TORNOU UMA LENDA...\n')
                        sleep(3)
                        print(' SEU CORPO POSSUI UMA AURA NEGRA E VERVELHA, SEUS OLHOS SÃO BRANCOS, E DELES SAEM')
                        print(' RAIOS QUE ESTRAÇALHAM AS ROCHAS AO SEU REDOR; \n')
                        sleep(3)
                        print(' FLUTUAMDO RENTE AO SOLO, NOSSO HERÓI ENCARA OS INIMIGOS...\n')
                        sleep(3)
                        print(' E EM FRAÇÃO DE SEGUNDOS OS ALCANÇA, DESFERINDO ATAQUES DE GRANDE PODER.\n')
                        sleep(3)
                        input(' PRESSIONE ENTER PARA CONTINUAR...\n')
                        sleep(1)
                        print('\n-----' + '::..::| MODO BESERKER ATIVADO |::..::' + '-----' + '\n')
                        sleep(3)
                        while n_rodadas_b < 2:
                            print('\n=====' + '.::| BESERKER RODADA {} |::.'.format(n_rodadas_b + 1) + '=====' + '\n')
                            sleep(2)
                            n_ataques = 1
                            print('.::| ATAQUES BESERKER |::.')
                            sleep(1)
                            tam_lista_inimigo = len(lista_inimigo)
                            while n_ataques <= tam_lista_inimigo:
                                escolhido = choice(lista_inimigo)
                                dano_b = randint(25, 40)
                                pv_i_antes = escolhido[1]
                                escolhido[1] -= dano_b
                                if n_rodadas_b == 0:
                                    dano_b_total_r1 += dano_b
                                elif n_rodadas_b == 1:
                                    dano_b_total_r2 += dano_b
                                print(f"\n Você causou {dano_b} de dano ao inimigo {escolhido[0]} ! ({pv_i_antes} - {dano_b} = {escolhido[1]})")
                                if n_inimigos < 50:
                                    sleep(0.5)
                                elif n_inimigos < 100:
                                    sleep(0.25)
                                else:
                                    sleep(0.1)
                                if escolhido[1] <= 0:
                                    str_inimigo = str(escolhido[0])
                                    tam_str_inimigo = len(str_inimigo)
                                    msg_morte = '   Voce matou o inimigo {}!'.format(str_inimigo)
                                    tam_msg_morte = len(msg_morte)
                                    print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1))
                                    print(msg_morte)
                                    print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1))
                                    if n_inimigos < 50:
                                        sleep(0.5)
                                    elif n_inimigos < 100:
                                        sleep(0.25)
                                    else:
                                        sleep(0.1)
                                    lista_inimigo.remove(escolhido)
                                    n_inimigos -= 1
                                    if n_rodadas_b == 0:
                                        cont_morte_r1 += 1
                                    elif n_rodadas_b == 1:
                                        cont_morte_r2 += 1
                                    if n_inimigos == 0:
                                        sleep(3)
                                        print('\n Nº Inimigos = 0\n')
                                        print(' .::| PARABÉNS, VOCÊ MATOU TODOS OS INIMIGOS |::.')
                                        sleep(1)
                                        restart = valida_str('JS', ' (J)ogar novamente ou (S)air:\n')
                                        if restart == 'J':
                                            jogando = True
                                        elif restart == 'S':
                                            jogando = False
                                        break
                                n_ataques += 1

                            if n_inimigos == 0:
                                break
                            print(f'\n\n.::| FIM DA RODADA {n_rodadas_b + 1} |::.')
                            sleep(3)
                            n_rodadas_b += 1

                        if n_inimigos == 0:
                            break
                        dano_b_total = dano_b_total_r1 + dano_b_total_r2
                        total_morte = cont_morte_r1 + cont_morte_r2
                        vida_drenada = round(0.1 * dano_b_total)
                        player_vida += vida_drenada
                        player_sp = 0
                        print('\n\n-----' + '.::| MODO BESERKER DESATIVADO |::.' + '-----' + '\n\n\n')
                        print('xxxxx' + '.::| ESTATÍSTICA BESERKER |::.' + 'xxxxx' + '\n\n')
                        print(f' - MORTES DA RODADA 1 = {cont_morte_r1}\n')
                        print(f' - MORTES DA RODADA 2 = {cont_morte_r2}\n')
                        print(f' - DANO DA RODADA 1 = {dano_b_total_r1}\n')
                        print(f' - DANO DA RODADA 2 = {dano_b_total_r2}\n')
                        print(f' - TOTAL DE MORTES = {total_morte}\n')
                        print(f' - INIMIGOS RESTANTES = {n_inimigos}\n')
                        print(f' - TOTAL DE DANO = {dano_b_total}\n')
                        print(f' - PONTOS DE VIDA DRENADOS = {vida_drenada}\n')
                        print(f' - VIDA = {player_vida}\n')
                        print(f' - SP = {player_sp}\n')
                        print('x' * 39 + '\n\n')
                        input(' .::| Precione ENTER para continuar jogando |::.\n')
                else:
                    print(f'\n Inimigo {i[0]} ERROU o ataque!')
                    if n_inimigos <= 20:
                        sleep(0.5)
                    elif n_inimigos <= 50:
                        sleep(0.25)
                    else:
                        sleep(0.125)
                if n_rodadas_b == 2:
                    break

        if n_rodadas_b != 2:
            print(f'\n DANO TOTAL = {soma_dano_inimigo}')
            sleep(3)
            print('=' * 33)
        if n_inimigos == 0:
            break
        elif player_vida <= 0:
            print('\nVIDA = 0\n')
            print(' .::| GAME OVER |::.\n')
            sleep(3)
            restart = valida_str('JS', ' (J)ogar novamente ou (S)air:\n')
            if restart == 'J':
                jogando = True
            elif restart == 'S':
                jogando = False
            break
        if n_rodadas_b != 2:
            player_sp += 3
            if player_sp > 100:
                player_sp = 100
        n_rodadas += 1

print('\n -FIM-')
sleep(3)
