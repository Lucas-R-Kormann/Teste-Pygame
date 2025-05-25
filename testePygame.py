import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

larguraTela = 640
alturaTela = 480

x_cobra = int(larguraTela/2 - 40)
y_cobra = int(alturaTela/2 - 50)

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)

y_maca = randint(50, 430)

fonte = pygame.font.SysFont("arial", 40, bold = True, italic = True)

pontos = 0

tela = pygame.display.set_mode((larguraTela, alturaTela))

pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 0, 255), (XeY[0], XeY[1], 20, 20))

lista_cobra = []
comprimento_inicial = 5

while True:
    relogio.tick(30)
    tela.fill((0, 255, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    
    cobra = pygame.draw.rect(tela, (0, 0, 255), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela,(255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        comprimento_inicial = comprimento_inicial + 1

    lista_posicao = []
    lista_posicao.append(x_cobra)
    lista_posicao.append(y_cobra)

    lista_cobra.append(lista_posicao)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (420, 40))

    pygame.display.update()

