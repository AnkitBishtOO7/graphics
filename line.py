import pygame
import sys

def bresenham_line(screen, x1, y1, x2, y2, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        screen.set_at((x1, y1), color)
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

def main():
    # line parameters
    x1 = int(input("Enter the x-coordinate of the start point: "))
    y1 = int(input("Enter the y-coordinate of the start point: "))
    x2 = int(input("Enter the x-coordinate of the end point: "))
    y2 = int(input("Enter the y-coordinate of the end point: "))
    print("switch to pygame terminal to see results")

    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Bresenham\'s Line Algorithm')

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    running = True
    screen.fill(WHITE)
    
    bresenham_line(screen, x1, y1, x2, y2, BLACK)
    
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

