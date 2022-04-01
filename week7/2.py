import pygame 
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("universe_vniumR1y.mp3")
pygame.mixer.music.play(-1)

right = 2
left = 2
cnt = 2
W, H = 500, 300
screen = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if cnt % 2 == 0:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
            cnt = cnt + 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if left % 2 == 0:
                pygame.mixer.music.load("htc_basic.mp3")
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.load("universe_vniumR1y.mp3")
                pygame.mixer.music.play(-1)
            left = left + 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if right % 2 == 0:
                pygame.mixer.music.load("universe_vniumR1y.mp3")
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.load("Sound_10457.mp3")
                pygame.mixer.music.play(-1)
            right = right + 1


        

    clock.tick(FPS)


