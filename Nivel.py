import pygame
class Pantalla:
    def __init__(self, screen):
        self.screen = screen


        self.current_level = 1
          #piso 1 
        self.size_cubo = 128
        self.pantalla_ancho = 1800
        self.pantalla_alto = 893
        #nivel 1
        self.cubo1 = pygame.image.load("../mio_ultimo/images/imagesuno/png/Tiles/Tile (1).png")
        self.cubo2 = pygame.image.load("../mio_ultimo/images/imagesuno/png/Tiles/Tile (2).png")
        self.cubo3 = pygame.image.load("../mio_ultimo/images/imagesuno/png/Tiles/Tile (2).png")
        self.arboles = pygame.image.load("../mio_ultimo/images/imagesuno/png/Objects/Tree.png ")
        self.cubo4 = pygame.image.load("../mio_ultimo/images/imagesuno/png/Tiles/Tile (2).png")
        self.cubo5 = pygame.image.load("../mio_ultimo/images/imagesuno/png/Tiles/Tile (2).png")

        #nivel 2
        self.cubo12 = pygame.image.load("../mio_ultimo/images/imagesdos/piso/1.png")
        self.cubo22 = pygame.image.load("../mio_ultimo/images/imagesdos/piso/2.png")
        self.cubo32 = pygame.image.load("../mio_ultimo/images/imagesdos/piso/3.png")
        self.direccion2 = pygame.image.load("../mio_ultimo/images/imagesdos/objects/Sign_2.png")
        self.fin2 = pygame.image.load("../mio_ultimo/images/imagesdos/objects/Sign_1.png")
        self.arboles2 = pygame.image.load("../mio_ultimo/images/imagesdos/objects/Tree_1.png")
        self.arbol2 = pygame.image.load("../mio_ultimo/images/imagesdos/objects/Tree_2.png")

        #nivel 3
        self.cubo13 = pygame.image.load("../mio_ultimo/images/imagestres/png/Tile/1.png")
        self.cubo23 = pygame.image.load("../mio_ultimo/images/imagestres/png/Tile/2.png")
        self.cubo33 = pygame.image.load("../mio_ultimo/images/imagestres/png/Tile/2.png")
        self.direccion3 = pygame.image.load("../mio_ultimo/images/imagestres/png/Objects/SignArrow.png")
        self.fin3 = pygame.image.load("../mio_ultimo/images/imagestres/png/Objects/Sign.png")
        self.arboles3 = pygame.image.load("../mio_ultimo/images/imagestres/png/Objects/Tree.png")
        self.arboles23 = pygame.image.load("../mio_ultimo/images/imagestres/png/Objects/Tree.png")
#/////////////////////////


    def inicio(self):
        for x in range(0, self.pantalla_ancho, self.size_cubo):
            self.screen.blit(self.cubo2, (x, self.pantalla_alto - self.size_cubo))

     
    def nivel_Dos(self):
        self.screen.blit(self.direccion2,[128*0, self.pantalla_alto-self.size_cubo*2+40])
        self.screen.blit(self.cubo12,[128*0, self.pantalla_alto-self.size_cubo])
        self.screen.blit(self.cubo22,[128*1, self.pantalla_alto-self.size_cubo])
        self.screen.blit(self.cubo32,[128*2, self.pantalla_alto-self.size_cubo])

        self.screen.blit(self.cubo12,[128*5, self.pantalla_alto-self.size_cubo])
        self.screen.blit(self.cubo22,[128*6, self.pantalla_alto-self.size_cubo])
        self.screen.blit(self.cubo22,[128*7, self.pantalla_alto-self.size_cubo])
        self.screen.blit(self.arboles2,[128*7-60, self.pantalla_alto-self.size_cubo*3])
        self.screen.blit(self.cubo32,[128*8, self.pantalla_alto-self.size_cubo])

        self.screen.blit(self.cubo12,[128*10, self.pantalla_alto-self.size_cubo])
        self.screen.blit(self.arboles2,[128*10, self.pantalla_alto-self.size_cubo*3])
        self.screen.blit(self.cubo22,[128*11, self.pantalla_alto-self.size_cubo])
        self.screen.blit(self.cubo22,[128*12, self.pantalla_alto-self.size_cubo])
        self.screen.blit(self.cubo22,[128*13, self.pantalla_alto-self.size_cubo])

        self.screen.blit(self.fin2, [128*13, self.pantalla_alto-self.size_cubo*2+40])

        self.screen.blit(self.cubo22,[128*14, self.pantalla_alto-self.size_cubo])

    def nivel_Tres(self):
        for x in range(0, self.pantalla_ancho, self.size_cubo):
            self.screen.blit(self.cubo13, (x, self.pantalla_alto - self.size_cubo))
