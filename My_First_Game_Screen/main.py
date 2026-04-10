import pygame

pygame.init()

# Create window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Game Screen")

running = True
while running:
    screen.fill((255, 255, 255))  # white background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()