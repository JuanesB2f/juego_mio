import pygame
import Music

class Enemy:
    def __init__(self, screen):
        self.caja = pygame.image.load("../mio_ultimo/images/imagesuno/png/Objects/Crate.png")
        self.cubo = pygame.image.load("../mio_ultimo/images/imagesuno/png/Objects/Crate.png")
        self.cube_size = 101
        self.pantalla_ancho = 1800
        self.pantalla_alto = 893
        self.x = self.pantalla_ancho - self.cube_size
        self.y = 0
        self.y_cubo = 0
        self.x_cubo = self.pantalla_ancho // 2
        self.screen = screen
        self.jumpCount = 10
        # Mover un objeto 0 derecha 1 izquierda
        self.direction = 0
        # Se crea el sonido
        self.music = Music.Music()

    # Método para mover el cubo
    def move(self):
        if self.direction == 0:  # Mover a la izquierda
            if self.x >= self.cube_size * 2 + 37:
                self.x -= 10
                self.y = 650
            else:
                self.direction = 1
        elif self.direction == 1:  # Rebotar hacia la derecha
            if self.x <= self.pantalla_ancho - self.cube_size:
                self.x += 15
            else:
                self.direction = 0

    # Método para dibujar el cubo
    def draw_cube(self):
        self.screen.blit(self.cubo, [self.x, self.y])

    # Método para dibujar la caja
    def draw_box(self):
        self.screen.blit(self.caja, [self.x_cubo, self.y_cubo])

    # Método para dibujar todo
    def draw_all(self):
        self.move()  # Llamada al método move() para mover la caja
        self.draw_box()
        self.draw_cube()


    # Método nuevo enemigo
    def movecube(self):
        self.screen.blit(self.cubo, [self.x_cubo, self.y_cubo])
        if self.direction == 0:
            if self.y_cubo <= self.pantalla_alto // 2 - 101 - 101:
                self.y_cubo += 15
            else:
                if self.x_cubo == self.pantalla_ancho // 2 - 20:
                    self.music.colision()
                if self.x_cubo > self.pantalla_ancho // 2 - 128 * 2 - 101:
                    self.x_cubo -= 15
                else:
                    if self.y_cubo <= self.pantalla_alto - self.cube_size * 2 - 4:
                        self.y_cubo += 15
                    else:
                        if self.x_cubo == self.pantalla_ancho - 128 - 110:
                            self.music.colision()
                        self.x_cubo -= 15
                        if self.x_cubo < 0 - self.cube_size:
                            self.x_cubo = self.pantalla_ancho // 2 - 20
                            self.y_cubo = 0
                            self.direction = 1
        else:
            if self.y_cubo <= self.pantalla_alto // 2 - 101 - 101:
                self.y_cubo += 15
            else:
                if self.x_cubo == self.pantalla_ancho // 2 - 20:
                    self.music.colision()
                if self.x_cubo < self.pantalla_ancho // 2 + 101:
                    self.x_cubo += 15
                else:
                    if self.y_cubo <= self.pantalla_alto - self.cube_size * 2 - 4:
                        self.y_cubo += 15
                    else:
                        if self.x_cubo == self.pantalla_ancho - 128 - 110:
                            self.music.colision()
                        self.x_cubo += 15
                        if self.x_cubo > self.pantalla_ancho:
                            self.x_cubo = self.pantalla_ancho // 2 - 20
                            self.y_cubo = 0
                            self.direction = 0

    def colisiones(self, rect, jugador):
        # Se detecta el rectangulo del jugador
        player = pygame.Rect(self.x, self.y, self.cube_size, self.cube_size)
        caja = pygame.Rect(self.x_cubo, self.y_cubo, self.cube_size, self.cube_size)
        if player.collidelist([rect]) >= 0:
            jugador.update("stand_down")
            jugador.dead = False
            if self.jumpCount >= -10:
                rect.y += self.jumpCount * abs(self.jumpCount)
                self.music.muerte()
                self.jumpCount -= 1
        if caja.collidelist([rect]) >= 0:
            jugador.update("stand_down")
            jugador.dead = False
            if self.jumpCount >= -10:
                rect.y += self.jumpCount * abs(self.jumpCount)
                self.music.muerte()
                self.jumpCount -= 1