import pygame
pygame.init()
pygame.mixer.pre_init(frequency=44100)
pygame.mixer.init()
pygame.mixer.music.load('SSF.wav')

pygame.mixer.music.play(0)

