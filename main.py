# Jumpy! - platform game

import pygame as pg
import random
from settings import *


class Game:
    def __init__(self):
        self.running = True
        pg.init()
        pg.mixer.init()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.Group()
        self.playing = False
        # initalize game window
        pass

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.run()

        # Starts a new game
        pass

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

        # Game Loop
        pass

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            # check for closing the window
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

    def draw(self):
        # Game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        # *after* drawing everything
        pg.display.flip()

    def show_start_screen(self):
        # Game Splash Screen
        pass

    def show_go_screen(self):
        # Game  over screen
        pass


g = Game()

g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
