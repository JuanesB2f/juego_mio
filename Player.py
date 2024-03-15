import pygame
# No necesitas importar la clase Music aquí

# ****************************************************************
# Importando la clase música
from Music import Music

# ****************************************************************
class player(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("../mio_ultimo/images/imagesuno/player.png")
        self.sheet.set_clip(pygame.Rect(0, 152, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.isJump = False
        self.jumpCount = 10
        self.left_states = {
            0: (0, 76, 52, 76),
            1: (52, 76, 52, 76),
            2: (104, 76, 52, 76),
            3: (156, 76, 52, 76),
        }
        self.right_states = {
            0: (0, 152, 52, 76),
            1: (52, 152, 52, 76),
            2: (104, 152, 52, 76),
            3: (156, 152, 52, 76),
        }
        self.down_states = {
            0: (0, 0, 52, 76),
            1: (52, 0, 52, 76),
            2: (104, 0, 52, 76),
            3: (156, 0, 52, 76),
        }
        self.music = Music()
        self.pantallaplayer = 0
        self.dead = True
        self.size_cubo = 128

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def move(self, x):
    # Define la velocidad del personaje
        speed = 0  # Ajusta este valor según lo rápido que quieras que se mueva el personaje
    
        if x > 100 and self.dead:
            self.clip(self.right_states)
        # Incrementa la posición x con la velocidad
        if self.rect.x < 1800:
            self.rect.x += speed
        else:
            self.rect.x = 0
            self.pantallaplayer += 1

        if x < -100 and self.dead:
            self.clip(self.left_states)
        # Decrementa la posición x con la velocidad
        if self.rect.x > 100:
            self.rect.x -= speed

    def update(self, direction):
        if direction == "left":
            self.clip(self.left_states)
            if self.rect.x > 0:
                self.rect.x -= 10
        if direction == "down":
            self.clip(self.down_states)
        if direction == "right":
            self.clip(self.right_states)
            if self.rect.x < 1800:
                self.rect.x += 10
            else:
                self.rect.x = 0
                self.pantallaplayer += 1
        if direction == "stand_left":
            self.clip(self.left_states[0])
        if direction == "stand_right":
            self.clip(self.right_states[0])
        if direction == "stand_down":
            self.clip(self.down_states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.JOYBUTTONDOWN and self.dead:
            self.isJump = True
            self.music.saltar()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and self.dead:
                self.update("right")
            if event.key == pygame.K_LEFT and self.dead:
                self.update("left")
            if event.key == pygame.K_UP and self.dead:
                self.isJump = True
                self.music.saltar()
            if event.key == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and self.dead:
                    self.update("stand_right")
                if event.key == pygame.K_LEFT and self.dead:
                    self.update("stand_left")
            return self.pantallaplayer

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.rect.y -= 5
                self.jumpCount = 10
        self.image = self.sheet.subsurface(self.sheet.get_clip())