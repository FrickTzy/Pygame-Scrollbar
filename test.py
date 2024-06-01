import pygame
from pygame_scrollbar import ContentBar, ScrollBarManager
import sys

# Initialize Pygame
pygame.init()
width, height = 1600, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Pygame Structure")

content_bar_list = [ContentBar(size=(500, 100)) for _ in range(100)]
scroll_manager = ScrollBarManager(content_bar_list=content_bar_list, size=(width, 800), margin=50, position=(100, 100))

# Set up the display

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        scroll_manager.check_if_scroll(event=event)
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    scroll_manager.show(surface=screen, window_height=height)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

# Cleanup
pygame.quit()
sys.exit()
