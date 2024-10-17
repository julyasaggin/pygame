import pygame
from random import choice

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 400, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Cara ou Coroa')

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Fonte
fonte = pygame.font.Font(None, 36)

# Função para mostrar texto na tela
def mostrar_texto(texto, x, y):
    texto_surface = fonte.render(texto, True, preto)
    tela.blit(texto_surface, (x, y))

# Loop principal
jogando = True
while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

    # Limpa a tela
    tela.fill(branco)

    # Mostra instruções
    mostrar_texto('Escolha: (C)ara ou (C)oroa', 50, 50)

    # Espera a entrada do usuário
    letra_usuario = ''
    while letra_usuario not in ['c', 'C']:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False
            if evento.type == pygame.KEYDOWN:
                if evento.unicode in ['c', 'C', 'o', 'O']:
                    letra_usuario = evento.unicode

    # Processa a jogada
    movimentos = ['cara', 'coroa']
    movimento_geral = choice(movimentos)

    if letra_usuario in ['c', 'C']:
        jogada_usuario = 'cara'
    else:
        jogada_usuario = 'coroa'

    jogada_AI = 'coroa' if jogada_usuario == 'cara' else 'cara'

    # Exibe os resultados
    mostrar_texto(f'AI escolheu: {jogada_AI}', 50, 100)
    mostrar_texto(f'Usuário escolheu: {jogada_usuario}', 50, 150)
    mostrar_texto(f'Caiu: {movimento_geral}', 50, 200)

    if jogada_AI == movimento_geral:
        mostrar_texto('AI acertou! Usuário errou!', 50, 250)
    elif jogada_usuario == movimento_geral:
        mostrar_texto('Usuário acertou! AI errou!', 50, 250)

    pygame.display.flip()

    # Espera um pouco antes de reiniciar
    pygame.time.delay(3000)

# Encerra o Pygame
pygame.quit()
