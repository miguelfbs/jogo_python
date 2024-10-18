
import pygame #importa a biblioteca pygame para o script


# pygame configuração
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600)) #definição do tamanho da tela
pygame.display.set_caption('Jogo da Velha') #nome da janela do jogo
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans MS', 100, True, True) #importar fonte
running = True #variável de controle do status do jogo

personagem_x = fonte_quadrinhos.render('X', True, '#87CEFA')
personagem_y = fonte_quadrinhos.render('O', True, '#FF69B4')
cor_fundo = 1

while running:
    # controle de enventos no jgo
    for event in pygame.event.get():
        # pygame.QUIT significa que quando usuário clicar em X a tela fechará
        if event.type == pygame.QUIT:
            running = False
        # pygame.MOUSEBUTTONDOWN significa evento de click do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 3):
                cor_fundo = 1
 
 #tabuleiro
    screen.fill('#F0F8FF')
    pygame.draw.line(screen, '#FFD700', (200, 20), (200, 580), 10)
    pygame.draw.line(screen, '#FFD700', (400, 20), (400, 580), 10)
    pygame.draw.line(screen, '#FFD700', (20, 200), (580, 200), 10)
    pygame.draw.line(screen, '#FFD700', (20, 400), (580, 400), 10)

    # if cor_fundo == 1:
    #    screen.blit(personagem_x,(60, 30))
    # # elif cor_fundo == 2:
    #     screen.blit(personagem_y,(260,30))
    #     screen.blit(personagem_x,(60, 30))
    # # elif cor_fundo == 3:
    #     screen.blit(personagem_y,(260,30))
    #     screen.blit(personagem_x,(60, 30))
    #     screen.blit(personagem_x,(460,230))   
    # # elif cor_fundo == 4:
    screen.blit(personagem_y,(260,30))
    screen.blit(personagem_x,(60, 30))
    screen.blit(personagem_x,(460,230))   
    screen.blit(personagem_y,(260,230))
    screen.blit(personagem_y,(260,430))



    # flip() o display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita o fps para 60

pygame.quit()