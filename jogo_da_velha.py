
import pygame #importa a biblioteca pygame para o script


# pygame configuração
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600)) #definição do tamanho da tela
screen.fill ('#F5F5F5')
pygame.display.set_caption('Jogo da Velha') #nome da janela do jogo
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans MS', 100, True, True) #importar fonte
running = True #variável de controle do status do jogo

personagem_x = fonte_quadrinhos.render('X', True, '#87CEFA')
personagem_o = fonte_quadrinhos.render('O', True, '#FF69B4')
personagem_0 = fonte_quadrinhos.render(' ', True, '#FF69B4')
personagem_1 = fonte_quadrinhos.render('tente outra posição', True, '#FF69B4')

rodadas = 0
coordenada_x = 0
coordenada_y = 0
personagem = personagem_x
q1 = 11
q2= 22
q3 = 33
q4 = 44
q5 = 55
q6 = 66
q7 = 77
q8 = 88
q9 = 99

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
            # print ('coordenada_x ', click_pos[0])
            # print ('coordenada_y ', click_pos[1])
            coordenada_x = click_pos[0]
            coordenada_y = click_pos[1]

            # if personagem == personagem_x:
            #     personagem = personagem_o
            # else:
            #     personagem = personagem_x

            rodadas = rodadas + 1
            if (rodadas > 9):
                screen.fill ('#F5F5F5')
                rodadas = 0
            
            # if rodadas != 1:
            #     if personagem == personagem_x:
            #         personagem = personagem_o
            #     else:
            #         personagem = personagem_x
            # else:
            #     personagem = personagem_x

            if rodadas == 0:
                personagem = personagem_0
            elif rodadas == 1:
                personagem = personagem_x
            elif rodadas == 2: 
                personagem = personagem_o
            elif rodadas == 3: 
                personagem = personagem_x
            elif rodadas == 4: 
                personagem = personagem_o
            elif rodadas == 5: 
                personagem = personagem_x
            elif rodadas == 6: 
                personagem = personagem_o
            elif rodadas == 7: 
                personagem = personagem_x
            elif rodadas == 8: 
                personagem = personagem_o
            elif rodadas == 9: 
                personagem = personagem_x


        
#  #tabuleiro  
#                                        origem     destino
#                                        (coordenada_x , coordenada_y)    (coordenada_x , coordenada_y)
    # screen.fill('#F0F8FF')
    pygame.draw.line(screen, '#FFD700', (200, 20), (200, 580), 10)
    pygame.draw.line(screen, '#FFD700', (400, 20), (400, 580), 10)
    pygame.draw.line(screen, '#FFD700', (20, 200), (580, 200), 10)
    pygame.draw.line(screen, '#FFD700', (20, 400), (580, 400), 10)


#posição personagens 

    if coordenada_x < 200 and coordenada_x > 0 and coordenada_y < 200:
        screen.blit(personagem,(60, 30)) #1 
        if personagem == personagem_x:
            q1 = 1
        else:
            q1 = 2
            
    elif coordenada_x > 200 and coordenada_x < 400 and coordenada_y < 200:
        screen.blit(personagem,(260,30)) #2
        if personagem == personagem_x:
            q2 = 1
        else:
            q2 = 2

    elif coordenada_x > 400 and coordenada_x < 600 and coordenada_y < 200:
        screen.blit(personagem,(460,30)) #3
        if personagem == personagem_x:
            q3 = 1
        else:
            q3 = 2

    elif coordenada_x < 200 and coordenada_y > 200 and coordenada_y < 400:
        screen.blit(personagem,(60,230)) #4
        if personagem == personagem_x:
            q4 = 1
        else:
            q4 = 2

    elif coordenada_x > 200 and coordenada_x < 400 and coordenada_y > 200 and coordenada_y < 400:
        screen.blit(personagem,(260,230)) #5
        if personagem == personagem_x:
            q5 = 1
        else:
            q5 = 2

    elif coordenada_x > 400 and coordenada_y > 200 and coordenada_y < 400:
        screen.blit(personagem,(460,230)) #6
        if personagem == personagem_x:
            q6 = 1
        else:
            q6 = 2

    elif coordenada_x < 200 and coordenada_y > 400:
        screen.blit(personagem,(60,430)) #7
        if personagem == personagem_x:
            q7 = 1
        else:
            q7 = 2

    elif coordenada_x > 200 and coordenada_x < 400 and coordenada_y > 400:
        screen.blit(personagem,(260,430)) #8
        if personagem == personagem_x:
            q8 = 1
        else:
            q8 = 2

    elif coordenada_x > 400 and coordenada_y > 400:
        screen.blit(personagem,(460,430)) #9
        if personagem == personagem_x:
            q9 = 1
        else:
            q9 = 2


    #vencedor
    # if q1 != q2 != q3 != q4 != q5 != q6 != q7 != q8 != q9:
    #     q1 = 11
    #     q2 = 22
    #     q3 = 33
    #     q4 = 44
    #     q5 = 55
    #     q6 = 66
    #     q7 = 77
    #     q8 = 88
    #     q9 = 99

    if q1 == q2 == q3:
        rodadas = 9
        q1 = 11
        q2 = 22
        q3 = 33
        pygame.draw.line(screen, '#FFD700', (20, 100), (580, 100), 10)
            

    # flip() o display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita o fps para 60

pygame.quit()