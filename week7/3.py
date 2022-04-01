import pygame
pygame.init()
X_width = 600
Y_width = 600
screen = pygame.display.set_mode((X_width, Y_width))
done = False
x = 50
y = 50

radius = 25
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP] and y > 30: y -= 20  
    if pressed[pygame.K_DOWN] and y < Y_width - 30: y += 20    
    if pressed[pygame.K_LEFT] and x > 30: x -= 20    
    if pressed[pygame.K_RIGHT] and x < X_width - 30: x += 20   
    pygame.draw.circle(screen, (255, 0, 0),  (x, y),radius)
    pygame.display.update()
    pygame.time.Clock().tick(60)
    color = (255 ,255, 255)
    screen.fill(color)
pygame.display.flip()