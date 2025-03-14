import pygame
import random

from constants import ASTEROID_MIN_RADIUS

from circleshape import CircleShape

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

  def update(self, dt):
    self.position += self.velocity * dt
  
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    random_angle = random.uniform(20, 50)
    random_rotation_1 = self.velocity.rotate(random_angle)
    random_rotation_2 = self.velocity.rotate(-random_angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    Asteroid(self.position.x, self.position.y, new_radius).velocity = random_rotation_1 * 1.2
    Asteroid(self.position.x, self.position.y, new_radius).velocity = random_rotation_2 * 1.2