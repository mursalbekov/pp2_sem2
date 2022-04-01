import pygame 
import datetime 

window = pygame.display.set_mode((1116,720))
img = pygame.image.load('layer.png')

left = pygame.image.load('left_hand.png')
right =  pygame.image.load('right_hand.png')

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.blit(img,(0,0))
    t = datetime.datetime.now()
    
    angle_second = t.second*6
    angle_minute = t.minute*6
    rot_image = pygame.transform.rotate(left,-angle_second)
    rot_image2 = pygame.transform.rotate(right,-angle_minute)
    window.blit(rot_image, rot_image.get_rect(center=left.get_rect(center=(558, 360)).center).topleft)
    window.blit(rot_image2, rot_image2.get_rect(center=right.get_rect(center=(558, 360)).center).topleft)

    pygame.display.update()

clock.tick(FPS)