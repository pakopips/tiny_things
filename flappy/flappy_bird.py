"""
Flappy Bird no Python
"""

#importando as libs
#pip install pygame
import pygame
import random

#Tela
LARGURA, ALTURA = 400, 600

#Cores RGB
AZUL = (135, 206, 250)
VERDE = (0, 200, 0)
AMARELO = (255, 255, 0)
PRETO = (0,0,0)

#Jogo
GRAVIDADE = 0.5
TAMANHO_PASSARO = 20
ESPACO_CANOS = 200
LARGURA_CANO = 60 
VELOCIDADE_CANO = 5
ALTURA_PULO = -10


pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Bird")
fonte = pygame.font.SysFont(name="Arial", size= 36)
relogio = pygame.time.Clock()

def resetar_jogo():
    global passaro_y, velocidade, cano_x, cano_altura, pontos, ja_contou_ponto
    passaro_y = ALTURA // 2
    velocidade = 0 
    cano_x = LARGURA
    cano_altura = random.randint(150,450)
    pontos = 0 
    ja_contou_ponto = False

def desenhar_texto(texto, fonte, cor, y):
    render = fonte.render(texto, True, cor)
    rect = render.get(texto, True, cor)
    tela.blit(render, rect)
    return rect

PASSARO_X = 50
passaro_y = ALTURA // 2
velocidade = 0

resetar_jogo()

cano_x = LARGURA
cano_altura = random.randint(a=150, b=450)

pontos = 0
ja_contou_ponto = False

rodando = True
estado = "menu"

while rodando:
    relogio.tick(60)
    tela.fill(AZUL)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            velocidade = -10


    velocidade += GRAVIDADE
    passaro_y += velocidade

    pygame.draw.circle(tela, AMARELO, (PASSARO_X, int(passaro_y)), TAMANHO_PASSARO)

    cano_x -= VELOCIDADE_CANO

    if cano_x + LARGURA_CANO < 0:
        cano_x = LARGURA
        ja_contou_ponto = False  
        cano_altura = random.randint(a=150,b=450)

    pygame.draw.rect(tela, VERDE, rect=(cano_x, 0, LARGURA_CANO, cano_altura))
    pygame.draw.rect(tela, VERDE, rect=(cano_x, cano_altura + ESPACO_CANOS, LARGURA_CANO, ALTURA))

    colidiu_horizontal = (
        PASSARO_X + TAMANHO_PASSARO > cano_x and
        PASSARO_X - TAMANHO_PASSARO < cano_x + LARGURA_CANO
    )

    colidiu_vertical = (
        passaro_y - TAMANHO_PASSARO < cano_altura or
        passaro_y + TAMANHO_PASSARO > cano_altura + ESPACO_CANOS
    )

    colidiu_cano = colidiu_horizontal and colidiu_vertical
    fora_da_tela = passaro_y > ALTURA or passaro_y < 0


    if colidiu_cano or fora_da_tela:
        rodando = False

    if cano_x + LARGURA_CANO < PASSARO_X and not ja_contou_ponto:
        pontos += 1
        ja_contou_ponto = True

    texto = fonte.render(f"Pontos: {pontos}", True, PRETO)   
    tela.blit(texto, (10, 10))


    pygame.display.update()

pygame.quit()


