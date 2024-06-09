import pygame
import sys

def draw_circle(screen, xc, yc, x, y, color):
    screen.set_at((xc + x, yc + y), color)
    screen.set_at((xc - x, yc + y), color)
    screen.set_at((xc + x, yc - y), color)
    screen.set_at((xc - x, yc - y), color)
    screen.set_at((xc + y, yc + x), color)
    screen.set_at((xc - y, yc + x), color)
    screen.set_at((xc + y, yc - x), color)
    screen.set_at((xc - y, yc - x), color)

def bresenham_circle(screen, xc, yc, r, color):
    x = 0
    y = r
    d = 3 - 2 * r
    draw_circle(screen, xc, yc, x, y, color)
    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        draw_circle(screen, xc, yc, x, y, color)

def main():
    # circle parameters
    xc = int(input("Enter the x-coordinate of the circle center: "))
    yc = int(input("Enter the y-coordinate of the circle center: "))
    r = int(input("Enter the radius of the circle: "))
    print("switch to pygame terminal to see results")

    # pygame terminal initializing
    pygame.init()

    # Screen dimensions
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Bresenham\'s Circle Algorithm')

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    running = True
    screen.fill(WHITE)
    
    bresenham_circle(screen, xc, yc, r, BLACK)
    
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
