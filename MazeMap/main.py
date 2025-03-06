import pygame
import os
import win32gui
import win32con
# Initialize Pygame
pygame.init()

# Load the image
image = pygame.image.load('map.png')

# Get the image size
image_rect = image.get_rect()

# Set the window position to the top right corner
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1590,10)

# Set up the display
screen = pygame.display.set_mode((image_rect.width, image_rect.height), pygame.NOFRAME)





# Main loop
running = True
while running:
    # Set the window to be always on top
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the image
    screen.blit(image, (0, 0))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()