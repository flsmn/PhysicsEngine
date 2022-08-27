import pygame, sys
import numpy as np

pygame.init()
clock = pygame.time.Clock()

screen_width, screen_height = 900, 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PhysicsEngine")

obj_list = []

class Object():
    def __init__(self, pos, vel, mass):
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.mass = mass

        self.gravity = np.array([0, 9.81])
        obj_list.append(self)
        
    def update_pos(self,dt):
        self.pos += self.vel * dt + 1/2 * self.gravity * dt**2

class Solver():
    def update(self,dt):
        self.update_pos(dt)
        self.applyBoundary()

    def update_pos(dt):
        for obj in obj_list:
            obj.update_pos(dt)

    def applyBoundary():
        center = np.array([screen_width/2,screen_height/2])
        radius = 300
        for obj in obj_list:
            center_to_obj = obj.pos - center
            dist = np.sqrt(center_to_obj.dot(center_to_obj))
            if dist > (radius - 10):
                n = center_to_obj/dist
                obj.pos = center + n * (radius - 10)

def draw(surface):
    screen.fill((0,0,0))
    pygame.draw.circle(surface, (255,255,255),[screen_width/2, screen_height/2], 300)
    for obj in obj_list:
        pygame.draw.circle(surface, (255,0,0), obj.pos, 10)

def fps_counter(font_fps):
    fps = str(int(clock.get_fps()))
    text = font_fps.render(fps, True, (255,0,0))
    screen.blit(text, (20,20))

def main():
    Object([400,200],[0,0],1)
    Object([200,200],[0,0],1)
    font_fps = pygame.font.SysFont("Arial", 25)
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        Solver.update(Solver,1)

        draw(screen)
        fps_counter(font_fps)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()








