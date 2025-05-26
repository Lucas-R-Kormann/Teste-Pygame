import pygame
from pygame.locals import *
from sys import exit
from random import randint # Importa as funcionalidades do Pygame

pygame.init() # Inicia o código

larguraTela = 640
alturaTela = 480 # Definição do tamanho da tela

x_cobra = int(larguraTela/2 - 20)
y_cobra = int(alturaTela/2 - 20) # Definição para a cobra aparecer no meio da tela

velocidade = 10
x_controle = velocidade
y_controle = 0 # Definição da velocidade

x_maca = randint(40, 600)
y_maca = randint(50, 430) # Definição de onde a maçã pode ou não aparecer (usando o randint para ser aleatório)

fonte = pygame.font.SysFont("arial", 40, bold=True, italic=True) 
pontos = 0 # Definição da fonte que será utilizada para mostrar os pontos e o seu valor inicial que é 0

tela = pygame.display.set_mode((larguraTela, alturaTela)) # Mostra a tela 
pygame.display.set_caption("Snake Game") # Nome que irá aparecer quando abrir a janela
relogio = pygame.time.Clock() # Conta a quantidade de FPS do jogo (frames por segundo)
lista_cobra = [] # Lista para armazenar a posição do corpo da cobra na tela
comprimento_inicial = 5 # Definição do comprimento inicial da cobra
morreu = False # Variável para quando o jogador morrer, inicialmente falso

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 0, 255), (XeY[0], XeY[1], 20, 20)) #Função para aumentar o tamanho da cobra quando comer uma maçã

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_posicao, x_maca, y_maca, morreu, x_controle, y_controle
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(larguraTela/2)
    y_cobra = int(alturaTela/2) 
    lista_cobra = []
    lista_posicao = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False
    x_controle = velocidade
    y_controle = 0 # Função para reiniciar o jogo, resetando todos os parâmetros 

while True: # O jogo deve estar dentro de um loop while para que continue funcionando
    relogio.tick(30) # Quantidade de FPS do jogo 
    tela.fill((0, 255, 0)) # Fundo da tela
    mensagem = f'Pontos: {pontos}' 
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255)) #Variável que define o texto dos pontos
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit() # Caso o jogador clique para fechar, o jogo fecha

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
                    x_controle = 0 # Definição para que a cobra se movimente ao pressionar as telcas WASD

    if not morreu:
        x_cobra += x_controle
        y_cobra += y_controle

        # Verifica se a cobra bateu nas paredes
        if x_cobra >= larguraTela or x_cobra < 0 or y_cobra >= alturaTela or y_cobra < 0:
            morreu = True

        cobra = pygame.draw.rect(tela, (0, 0, 255), (x_cobra, y_cobra, 20, 20)) # Mostra a cobra na tela
        maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20)) # Mostra a maçã na tela

        if cobra.colliderect(maca):
            x_maca = randint(40, 600)
            y_maca = randint(50, 430)
            pontos += 1
            comprimento_inicial += 1 # Verifica quando a cobra come a maçã e aumenta seu tamanho

        lista_posicao = [x_cobra, y_cobra] # Lista para armazenar a posição da cabeça da cobra
        lista_cobra.append(lista_posicao) # Lista para armazenar a posição do corpo da cobra em relação a posição da cabeça

        if lista_cobra.count(lista_posicao) > 1:
            morreu = True # Define que se a cobra encostar nela mesma, o jogo acaba

        if len(lista_cobra) > comprimento_inicial:
            del lista_cobra[0] # Faz com que a cobra não fique crescendo indefinidamente

        aumenta_cobra(lista_cobra)# Permite que a cobra cresça

        tela.blit(texto_formatado, (420, 40)) # Mostra os pontos na tela
    
    else:
        fonte2 = pygame.font.SysFont("arial", 20, True, True) # Definição do texto de game over
        mensagem = "Game Over! Pressione a tecla R para jogar novamente" # Mensagem quando o jogador perde
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0)) 
        ret_texto = texto_formatado.get_rect(center=(larguraTela/2, alturaTela/2)) # Variável para mostrar o texto de game over no centro da tela
        
        tela.fill((255, 255, 255)) # Deixa o fundo da tela branco quando o jogador morre
        tela.blit(texto_formatado, ret_texto) # Mostra a mensagem de game over para o jogador
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    reiniciar_jogo() #Define que se o jogador clicar para fechar a janela será fechada, ou se o jogador apertar R, o jogo reinicia

    pygame.display.update() # Atualiza a tela 

