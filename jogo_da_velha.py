import pygame #importa a biblioteca pygame para o script


# pygame configuração
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600)) #definição do tamanho da tela
screen.fill ('#151515')
pygame.display.set_caption('Jogo da Velha') #nome da janela do jogo
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans MS', 100, True, True) #importar fonte
running = True #variável de controle do status do jogo

personagem_x = fonte_quadrinhos.render('X', True, '#B31312')
personagem_o = fonte_quadrinhos.render('O', True, '#387ADF')

personagem = personagem_x

rodadas = 0
tabuleiro_desenhado = False
coordenada_x = 0
coordenada_y = 0

q1 = ''
q2 = ''
q3 = ''
q4 = ''
q5 = ''
q6 = ''
q7 = ''
q8 = ''
q9 = ''

#tabuleiro
def desenha_tabuleiro(espessura,cor):
    pygame.draw.line(screen, cor, (200, 20), (200, 580), espessura)
    pygame.draw.line(screen, cor, (400, 20), (400, 580), espessura)
    pygame.draw.line(screen, cor, (20, 200), (580, 200), espessura)
    pygame.draw.line(screen, cor, (20, 400), (580, 400), espessura)

#posição personagens 
def faz_jogada():
    global q1, q2, q3, q4, q5, q6, q7, q8, q9
    status = True
    if q1 == '' and coordenada_x > 0 and coordenada_x < 200 and coordenada_y< 200:
        screen.blit(personagem,(60,30))  #primeiro
        q1 = personagem
    elif q2 == '' and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y< 200:
        screen.blit(personagem,(260,30)) #segundo
        q2 = personagem
    elif q3 == '' and coordenada_x >= 400 and coordenada_y < 200:
        print ('jogada')
        screen.blit(personagem,(460,30)) #terceiro
        q3 = personagem
    elif q4 == '' and  coordenada_x < 200 and coordenada_y>= 200 and coordenada_y< 400:
        screen.blit(personagem,(60,230))  #quarto
        q4 = personagem
    elif q5 == '' and   coordenada_x >= 200 and coordenada_x < 400 and coordenada_y>= 200 and coordenada_y< 400:
        screen.blit(personagem,(260,230)) #quinto
        q5 = personagem
    elif q6 == '' and   coordenada_x >= 400 and coordenada_y>= 200 and coordenada_y< 400:
        screen.blit(personagem,(460,230)) #secoordenada_xto
        q6 = personagem
    elif q7 == '' and   coordenada_x < 200 and coordenada_y>= 400:
        screen.blit(personagem,(60,430))  #setimo
        q7 = personagem
    elif q8 == '' and   coordenada_x >= 200 and coordenada_x < 400 and coordenada_y>= 400:
        screen.blit(personagem,(260,430)) #oitavo
        q8 = personagem
    elif q9 == '' and   coordenada_x >= 400 and coordenada_y>= 400:
        screen.blit(personagem,(460,430)) #nono
        q9 = personagem
    else:
        status = False
    
    return status

def check_vencedor():
    if q1 == q2 == q3:
        print ('vencedor', personagem)
    elif q4 == q5 == q6:
        print ('vencedor', personagem)


while running:

    # controle de enventos no jgo
    for event in pygame.event.get():
        # pygame.QUIT significa que quando usuário clicar em X a tela fechará
        if event.type == pygame.QUIT:
            running = False
        # pygame.MOUSEBUTTONDOWN significa evento de click do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(rodadas)
            click_pos = pygame.mouse.get_pos()
            coordenada_x = click_pos[0]
            coordenada_y = click_pos[1]

            if (rodadas >= 9):
                print ('vencedor')
                screen.fill ('#151515')
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0
                print(coordenada_x)
                personagem = personagem_x
                tabuleiro_desenhado = False

            if(faz_jogada()):
                rodadas = rodadas + 1
                if personagem == personagem_x:
                    personagem = personagem_o
                else:
                    personagem = personagem_x

    #jogo
    if tabuleiro_desenhado == False:
        desenha_tabuleiro(10,'#EEE2DE')
        q1 = ''
        q2 = ''
        q3 = ''
        q4 = ''
        q5 = ''
        q6 = ''
        q7 = ''
        q8 = ''
        q9 = ''
        tabuleiro_desenhado = True
        

    #vencedor

    if q1 == q2 == q3 != '':
        rodadas = 9
        q1 = ''
        q2 = ''
        q3 = ''
        tabuleiro_desenhado = False
        pygame.draw.line(screen, '#EEE2DE', (20, 100), (580, 100), 10) 

    if q4 == q5 == q6 != '':
        rodadas = 9
        q4 = ''
        q5 = ''
        q6 = ''
        pygame.draw.line(screen, '#EEE2DE', (20, 300), (580, 300), 10)

    elif q7 == q8 == q9 != '':
        rodadas = 9
        q7 = ''
        q8 = ''
        q9 = ''
        pygame.draw.line(screen, '#EEE2DE', (20, 500), (580, 500), 10)

    elif q3 == q5 == q7 != '':
        rodadas = 9
        q7= ''
        q5 = ''
        q3 = ''
        pygame.draw.line(screen, '#EEE2DE', (30, 570), (570, 30), 15)
    
    elif q1 == q4 == q7 != '':
        rodadas = 9
        q1 = ''
        q4 = ''
        q7 = ''
        pygame.draw.line(screen, '#EEE2DE', (100, 20), (100, 580), 10)

    elif q1 == q5 == q9 != '':
        rodadas = 9
        q1 = ''
        q5 = ''
        q9 = ''
        pygame.draw.line(screen, '#EEE2DE', (20, 20), (570, 570), 15)

    elif q2 == q5 == q8 != '':
        rodadas = 9
        q2 = ''
        q5 = ''
        q8 = ''
        pygame.draw.line(screen, '#EEE2DE', (300, 20), (300, 580), 10)

    elif q3 == q6 == q9 != '':
        rodadas = 9
        q3 = ''
        q6 = ''
        q9 = ''
        pygame.draw.line(screen, '#EEE2DE', (500, 20), (500, 580), 10)

    pygame.display.flip()

    clock.tick(60)  # limita o fps para 60

pygame.quit()