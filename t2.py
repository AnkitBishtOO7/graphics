import pygame
import sys
from circle import bresenham_circle
from line import bresenham_line

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (119, 221, 119)
BLUE = (177, 156, 217)
GRAY = (173, 216, 230)
BUTTON_COLOR = GRAY
HOVER_COLOR = BLACK
TEXT_COLOR = BLUE
INPUT_COLOR = (200, 200, 200)
ACTIVE_INPUT_COLOR = WHITE

# Fonts
font = pygame.font.Font(None, 32)
big_font = pygame.font.Font(None, 64)

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CS Final Year Project")

def draw_button(text, rect, is_hovered):
    color = HOVER_COLOR if is_hovered else BUTTON_COLOR
    pygame.draw.rect(screen, color, rect)
    txt_surface = font.render(text, True, TEXT_COLOR)
    screen.blit(txt_surface, (rect.x + (rect.width - txt_surface.get_width()) // 2, rect.y + (rect.height - txt_surface.get_height()) // 2))

def draw_input_fields(prompts, inputs, active_input):
    input_fields = []
    for i, (prompt, input_text, active) in enumerate(zip(prompts, inputs, active_input)):
        txt_surface = font.render(prompt, True, TEXT_COLOR)
        screen.blit(txt_surface, (10, 100 + i * 50))
        input_rect = pygame.Rect(250, 100 + i * 50, 140, 32)
        pygame.draw.rect(screen, ACTIVE_INPUT_COLOR if active else INPUT_COLOR, input_rect)
        txt_surface = font.render(input_text, True, TEXT_COLOR)
        screen.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))
        input_fields.append(input_rect)
    return input_fields

def circle_screen():
    running = True
    input_texts = [""] * 3  # Initial empty text for input fields
    active_input = [False] * 3  # Track which input field is active for text input
    enter_button = pygame.Rect((WIDTH - 200) // 2, HEIGHT - 100, 200, 50)

    while running:
        screen.fill(GRAY)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if enter_button.collidepoint(event.pos):
                    bresenham_circle_screen(input_texts)
                for i, rect in enumerate(input_fields):
                    if rect.collidepoint(event.pos):
                        active_input = [False] * len(input_fields)
                        active_input[i] = True
                    else:
                        active_input[i] = False
            elif event.type == pygame.KEYDOWN:
                if any(active_input):
                    index = active_input.index(True)
                    if event.key == pygame.K_BACKSPACE:
                        input_texts[index] = input_texts[index][:-1]
                    else:
                        input_texts[index] += event.unicode

        # Draw heading
        heading_surface = big_font.render("Circle Input", True, BLACK)
        screen.blit(heading_surface, ((WIDTH - heading_surface.get_width()) // 2, 10))

        # Define input prompts
        prompts = ["Center X:", "Center Y:", "Radius:"]

        # Draw input fields
        input_fields = draw_input_fields(prompts, input_texts, active_input)

        # Draw Enter button
        mouse_pos = pygame.mouse.get_pos()
        draw_button("Enter", enter_button, enter_button.collidepoint(mouse_pos))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def bresenham_circle_screen(input_texts):
    running = True
    center_x, center_y, radius = map(int, input_texts)

    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the circle using Bresenham's algorithm
        bresenham_circle(screen, center_x, center_y, radius, BLACK)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def line_screen():
    running = True
    input_texts = [""] * 4  # Initial empty text for input fields
    active_input = [False] * 4  # Track which input field is active for text input
    enter_button = pygame.Rect((WIDTH - 200) // 2, HEIGHT - 100, 200, 50)

    while running:
        screen.fill(GRAY)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if enter_button.collidepoint(event.pos):
                    bresenham_line_screen(input_texts)
                for i, rect in enumerate(input_fields):
                    if rect.collidepoint(event.pos):
                        active_input = [False] * len(input_fields)
                        active_input[i] = True
                    else:
                        active_input[i] = False
            elif event.type == pygame.KEYDOWN:
                if any(active_input):
                    index = active_input.index(True)
                    if event.key == pygame.K_BACKSPACE:
                        input_texts[index] = input_texts[index][:-1]
                    else:
                        input_texts[index] += event.unicode

        # Draw heading
        heading_surface = big_font.render("Line Input", True, BLACK)
        screen.blit(heading_surface, ((WIDTH - heading_surface.get_width()) // 2, 10))

        # Define input prompts
        prompts = ["Start X:", "Start Y:", "End X:", "End Y:"]

        # Draw input fields
        input_fields = draw_input_fields(prompts, input_texts, active_input)

        # Draw Enter button
        mouse_pos = pygame.mouse.get_pos()
        draw_button("Enter", enter_button, enter_button.collidepoint(mouse_pos))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def bresenham_line_screen(input_texts):
    running = True
    start_x, start_y, end_x, end_y = map(int, input_texts)

    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the line using Bresenham's algorithm
        bresenham_line(screen, start_x, start_y, end_x, end_y, BLACK)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def main_screen():
    running = True
    while running:
        screen.fill(GRAY)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if circle_button.collidepoint(event.pos):
                    circle_screen()
                elif line_button.collidepoint(event.pos):
                    line_screen()
        
        # Draw heading
        heading_surface = big_font.render("CS Final Year Project", True, BLACK)
        screen.blit(heading_surface, ((WIDTH - heading_surface.get_width()) // 2, 50))
        mine = font.render("by Ankit", True, BLACK)
        screen.blit(mine, ((WIDTH - heading_surface.get_width()) // 2 + 500, 550))
        
        # Define buttons
        circle_button = pygame.Rect((WIDTH - 200) // 2, HEIGHT // 2 - 60, 200, 50)
        line_button = pygame.Rect((WIDTH - 200) // 2, HEIGHT // 2 + 10, 200, 50)
        
        # Check mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        # Draw buttons with hover effect
        draw_button("Circle", circle_button, circle_button.collidepoint(mouse_pos))
        draw_button("Line", line_button, line_button.collidepoint(mouse_pos))
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

# main screen function
if __name__ == "__main__":
    main_screen()
