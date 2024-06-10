import pygame

def bresenham_circle(screen, x0, y0, radius, color):
    x = 0
    y = radius
    d = 3 - 2 * radius
    while y >= x:
        screen.set_at((x0 + x, y0 + y), color)
        screen.set_at((x0 - x, y0 + y), color)
        screen.set_at((x0 + x, y0 - y), color)
        screen.set_at((x0 - x, y0 - y), color)
        screen.set_at((x0 + y, y0 + x), color)
        screen.set_at((x0 - y, y0 + x), color)
        screen.set_at((x0 + y, y0 - x), color)
        screen.set_at((x0 - y, y0 - x), color)
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1
