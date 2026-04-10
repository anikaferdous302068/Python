import pygame

pygame.init()

# Create window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Font for text
font = pygame.font.Font(None, 36)
text = font.render("Hello Game!", True, (0, 0, 0))

running = True
while running:
    screen.fill(WHITE)  # background

    # Draw rectangle at center
    rect = pygame.Rect(270, 190, 100, 100)
    pygame.draw.rect(screen, BLUE, rect)

    # Show text
    screen.blit(text, (250, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()