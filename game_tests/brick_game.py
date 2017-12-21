# coding: utf-8

import sys
import pygame
pygame.init()

size = width, height = 920, 740
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()


class Game (Scene):
    def setup(self):
        self.background_color = "#008209"
        ground = Node(parent=self)
        x = 0

        while x <= self.size.w + 64:
            tile = SpriteNode('plf:[Ground Image Here]', position=(x, 0))
            ground.add_child(tile)
            x += 64
            self.player = SpriteNode('plf:[eli2.jpg]')
            self.player.anchor_position = (0.5, 0)
            self.player.position = (self.size.w / 3, 32)
            self.add_child(self.player)

    if __name__ == '__main__':
        run(Game(), PORTRAIT, show_fps=True)
