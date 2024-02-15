import pygame
from dataclasses import dataclass
from math import *
from datetime import *
import numpy as np

G = 6.674 * (10 ** -11) # m^3 kg^-1 s^-2
EARTH_MOON_DISTANCE = 384400e3 # m
TIME = 60 # s

@dataclass
class Earth:
    mass: float = 5.972e24 # kg
    velocity: tuple = (0, 0) # m/s
    # position: tuple = (0, 0)
    position: tuple = (0, 0) # m

@dataclass
class Moon:
    mass: float = 7.342e22
    # start with realistic velocity
    velocity: tuple = (1022, 0)
    # position: tuple = (0, 0)
    position: tuple = (0, -EARTH_MOON_DISTANCE)

def normalize_position(obj, window_size):
    max_w = EARTH_MOON_DISTANCE * 4
    max_h = EARTH_MOON_DISTANCE * 4
    x, y = obj.position
    y += max_h / 4
    x = (x + max_w / 2) / max_w * window_size[0]
    y = (y + max_h / 2) / max_h * window_size[1] - window_size[1] / 4
    return (int(x), int(y))

def distance(moon, earth):
    x1, y1 = moon.position
    x2, y2 = earth.position
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def newton_law_equation(mass1, mass2, distance):
    return G * (mass1 * mass2) / (distance ** 2)

def earth_object(position, display):
    pygame.draw.circle(display, (0, 0, 255), position, 10)

def moon_object(position, display):
    pygame.draw.circle(display, (255, 255, 255), position, 2)

def acceleration(force, mass):
    return force / mass

def speed(acceleration):
    return acceleration * TIME

def position(prev, speed):
    return prev + speed * TIME

def norm(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5

def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def create_vector(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

# return the direction of a vector
# NE, NW, SE, SW
def vec_direction(v):
    if v[0] >= 0 and v[1] >= 0:
        return "NE"
    elif v[0] <= 0 and v[1] >= 0:
        return "NW"
    elif v[0] >= 0 and v[1] <= 0:
        return "SE"
    elif v[0] <= 0 and v[1] <= 0:
        return "SW"

def calc_angle(moon, earth, direction):
    vector = create_vector(moon.position, earth.position)
    if direction == "NE":
        return np.arccos(dot_product(vector, (1, 0)) / (norm(vector) * norm((1, 0))))
    elif direction == "NW":
        return np.arccos(dot_product(vector, (-1, 0)) / (norm(vector) * norm((-1, 0))))
    elif direction == "SE":
        return np.arccos(dot_product(vector, (1, 0)) / (norm(vector) * norm((1, 0))))
    elif direction == "SW":
        return np.arccos(dot_product(vector, (-1, 0)) / (norm(vector) * norm((-1, 0))))

def calc_fx(force, angle, direction):
    if direction == "NE":
        return force * np.cos(angle)
    elif direction == "NW":
        return -force * np.cos(angle)
    elif direction == "SE":
        return force * np.cos(angle)
    elif direction == "SW":
        return -force * np.cos(angle)

def calc_fy(force, angle, direction):
    if direction == "NE":
        return force * np.sin(angle)
    elif direction == "NW":
        return force * np.sin(angle)
    elif direction == "SE":
        return -force * np.sin(angle)
    elif direction == "SW":
        return -force * np.sin(angle)

def update_position(moon, earth):
    nf = newton_law_equation(moon.mass, earth.mass, distance(moon, earth))
    direction = vec_direction(create_vector(moon.position, earth.position))
    angle = calc_angle(moon, earth, direction)
    fx = calc_fx(nf, angle, direction)
    fy = calc_fy(nf, angle, direction)
    ax = acceleration(fx, moon.mass)
    ay = acceleration(fy, moon.mass)
    moon.velocity = (moon.velocity[0] + speed(ax), moon.velocity[1] + speed(ay))
    moon.position = (position(moon.position[0], moon.velocity[0]), position(moon.position[1], moon.velocity[1]))

def main():
    pygame.init()
    display_width, display_height = 1200, 900
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Gravity Simulator")
    font = pygame.font.SysFont(None, 25)
    earth = Earth()
    moon = Moon()
    t = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill((0, 0, 0))
        t += TIME
        time_passed_formatted = str(timedelta(seconds=t))
        display_text = font.render("TIME: " + time_passed_formatted, True, (255, 255, 255))
        gameDisplay.blit(display_text, [0, 0])
        earth_object(normalize_position(earth, (display_width, display_height)), gameDisplay)
        moon_object(normalize_position(moon, (display_width, display_height)), gameDisplay)
        pygame.display.update()
        update_position(moon, earth)

# def main():
#     print(calc_angle(Moon(), Earth()))
#     print(normalize_position(Moon(), (1200, 900)))

if __name__ == "__main__":
    main()
