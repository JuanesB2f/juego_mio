import pygame
import Player
import Enemy
import Nivel
import Music

pygame.init()

pantalla_ancho = 1800
pantalla_alto = 893
size = (pantalla_ancho, pantalla_alto)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pantalla_juego = Nivel.Pantalla(screen)
enemy = Enemy.Enemy(screen)
player = Player.player((0, pantalla_alto - 128 - 76))
music = Music.Music()

nivel = 0

bg = pygame.image.load("../mio_ultimo/images/imagesuno/png/BG.png").convert()

done = False

music.music_fondo()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(bg, [0, 0])

    if player.pantallaplayer == 0:
        pantalla_juego.inicio()

    if player.pantallaplayer > 0:
        pantalla_juego.nivel_Dos()

    if player.pantallaplayer > 1:  # Cambiado a 1 para nivel tres, ya que parece que nivel 1 es cuando player.pantallaplayer > 0
        pantalla_juego.nivel_Tres()

    enemy.draw_all()
    enemy.colisiones(player.rect, player)
    enemy.movecube()

    pantalla = player.handle_event(event)
    screen.blit(player.image, player.rect)
    player.jump()
     # Llamar a la función desde la instancia de luna

    pygame.display.flip()
    clock.tick(15)

pygame.quit()
