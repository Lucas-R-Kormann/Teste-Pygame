import pygame 
from pygame.locals import *
from sys import exit

pygame.init()

larguraTela = 640
alturaTela = 480
x = larguraTela/2 - 40
y = 0

tela = pygame.display.set_mode((larguraTela, alturaTela))

pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            exit()

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))

    if y >= alturaTela:
        y = 0
    y = y + 1

    pygame.display.update()
