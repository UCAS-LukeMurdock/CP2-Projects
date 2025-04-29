# Pygame
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))

background_image = pygame.image.load('Random/image.png')  # Load the image
background_image = pygame.transform.scale(background_image, (1200, 800))  # Scale to fit the screen

font = pygame.font.Font(None, 36)

def display(message):
    final_surface = font.render(message, True, (0, 0, 0))
    screen.fill((255, 255, 255))  # Clear the screen for the final message
    screen.blit(background_image, (0,0))
    screen.blit(final_surface, (50, 50))
    pygame.display.flip()  # Update the display
    pygame.time.delay(3000)  # Wait for 5 seconds before quitting

import pygame

def inputting():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Username Input")

    font = pygame.font.Font(None, 30)
    input_box = pygame.Rect(100, 100, 200, 30)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface = font.render(text, True, (0, 0, 0))
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.display.flip()
        return text

user = inputting()
display(user)