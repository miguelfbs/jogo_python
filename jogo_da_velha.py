
import pygame #importa a biblioteca pygame para o script


# pygame configuração
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600)) #definição do tamanho da tela
pygame.display.set_caption('Jogo da Xuxa') #nome da janela do jogo
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans MS', 100, True, True) #importar fonte
running = True #variável de controle do status do jogo

personagem_x = fonte_quadrinhos.render('X', True, '#87CEFA')
personagem_o = fonte_quadrinhos.render('O', True, '#FF69B4')
personagem_0 = fonte_quadrinhos.render(' ', True, '#FF69B4')

quadrante = 0
x = 0
y = 0
personagem = personagem_x
while running:
    # controle de enventos no jgo
    for event in pygame.event.get():
        # pygame.QUIT significa que quando usuário clicar em X a tela fechará
        if event.type == pygame.QUIT:
            running = False
        # pygame.MOUSEBUTTONDOWN significa evento de click do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(quadrante)
            click_pos = pygame.mouse.get_pos()
            # print ('x ', click_pos[0])
            # print ('y ', click_pos[1])
            x = click_pos[0]
            y = click_pos[1]

            quadrante = quadrante + 1
            if (quadrante > 9):
                screen.fill ('black')
                quadrante = 0
            
            if quadrante == 0:
                personagem = personagem_0
            elif quadrante == 1:
                personagem = personagem_x
            elif quadrante == 2: 
                personagem = personagem_o
            elif quadrante == 3: 
                personagem = personagem_x
            elif quadrante == 4: 
                personagem = personagem_o
            elif quadrante == 5: 
                personagem = personagem_x
            elif quadrante == 6: 
                personagem = personagem_o
            elif quadrante == 7: 
                personagem = personagem_x
            elif quadrante == 8: 
                personagem = personagem_o
            elif quadrante == 9: 
                personagem = personagem_x


        
#  #tabuleiro  
#                                        origem     destino
#                                        (x , y)    (x , y)
    # screen.fill('#F0F8FF')
    pygame.draw.line(screen, '#FFD700', (200, 20), (200, 580), 10)
    pygame.draw.line(screen, '#FFD700', (400, 20), (400, 580), 10)
    pygame.draw.line(screen, '#FFD700', (20, 200), (580, 200), 10)
    pygame.draw.line(screen, '#FFD700', (20, 400), (580, 400), 10)


#posição personagens 

    if x < 200 and x > 0 and y < 200:
        screen.blit(personagem,(60, 30)) #1 
        q1 = personagem
        print (q1)
    elif x > 200 and x < 400 and y < 200:
        screen.blit(personagem,(260,30)) #2

    elif x > 400 and x < 600 and y < 200:
        screen.blit(personagem,(460,30)) #3

    elif x < 200 and y > 200 and y < 400:
        screen.blit(personagem,(60,230)) #4

    elif x > 200 and x < 400 and y > 200 and y < 400:
        screen.blit(personagem,(260,230)) #5

    elif x > 400 and y > 200 and y < 400:
        screen.blit(personagem,(460,230)) #6

    elif x < 200 and y > 400:
        screen.blit(personagem,(60,430)) #7

    elif x > 200 and x < 400 and y > 400:
        screen.blit(personagem,(260,430)) #8

    elif x > 400 and y > 400:
        screen.blit(personagem,(460,430)) #9

   
    # flip() o display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita o fps para 60

pygame.quit()