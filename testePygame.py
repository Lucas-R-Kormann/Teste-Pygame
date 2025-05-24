import pygame 
import os
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

larguraTela = 640
alturaTela = 480
x = int(larguraTela/2 - 40)
y = int(alturaTela/2 - 50)

x_azul = randint(40, 600)

y_azul = randint(50, 430)

fonte = pygame.font.SysFont("arial", 40, bold = True, italic = True)

pontos = 0

tela = pygame.display.set_mode((larguraTela, alturaTela))

pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x = x - 10

    if pygame.key.get_pressed()[K_d]:
        x = x + 10

    if pygame.key.get_pressed()[K_w]:
        y = y - 10

    if pygame.key.get_pressed()[K_s]:
        y = y + 10

    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_azul = pygame.draw.rect(tela,(0, 0, 255), (x_azul, y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1

    tela.blit(texto_formatado, (420, 40))

    pygame.display.update()
