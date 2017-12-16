import pygame
pygame.init()
pygame.mixer.pre_init(frequency=44100)
pygame.mixer.init()
pygame.mixer.music.load('SSF.wav')

screen = pygame.display.set_mode((400, 300))
done = False
try:
    sound = pygame.mixer.music.play(1)
    sound.play(loops = -1)
except:
    print ("Cannot play sound")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
                                                                
    pygame.display.flip()


