import pygame


class Music:
    def __init__(self):
        # Variables de sonido
        self.jump = "../mio_ultimo/music/jump.mp3"
        self.fondo = "../mio_ultimo/music/fondo.mp3"
        self.golpe = "../mio_ultimo/music/golpe.mp3"
        self.muerte_sound = "../mio_ultimo/music/muerte.mp3" # Cambio de nombre de variable

    # ****************************************************************
    # Método saltar
    def saltar(self):
        # Se inicializa el sonido
        pygame.mixer.init()
        # Se agrega el sonido
        pygame.mixer.music.load(self.jump)
        # Cuantas veces se genera el sonido
        pygame.mixer.music.play(1)

    # ****************************************************************
    # Método musica de fondo
    def music_fondo(self):
        # Se inicializa el sonido
        pygame.mixer.init()
        # Se agrega el sonido
        pygame.mixer.music.load(self.fondo)
        # Modificando el volumen
        pygame.mixer.music.set_volume(0.2)
        # Cuantas veces se genera el sonido
        pygame.mixer.music.play()

    # ****************************************************************
    # Golpe
    def colision(self):
        # Se inicializa el sonido
        pygame.mixer.init()
        # Se agrega el sonido
        colision_sound = pygame.mixer.Sound(self.golpe) # Uso de Sound en lugar de music
        # Cuantas veces se genera el sonido
        colision_sound.play()

    def muerte(self):
        # Se inicializa el sonido
        pygame.mixer.init()
        # Se agrega el sonido
        pygame.mixer.music.load(self.muerte_sound) # Se carga muerte_sound en lugar de dead
        # Cuantas veces se genera el sonido
        pygame.mixer.music.play(1)