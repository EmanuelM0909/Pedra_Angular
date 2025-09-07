import pygame
# inicia o pygame
pygame.init()
# carrega o arquivo mp3
pygame.mixer.music.load("ex021.mp3")
# toca a música (0 significa tocar apenas 1 vez)
pygame.mixer.music.play()
# Enquanto a música estiver tocando, o programa fica preso aqui
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # aguarda um pouco para não travar o PC
