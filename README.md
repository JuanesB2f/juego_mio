##DIAGRAMS

'''mermaid
classDiagram
    class Pantalla {
        -screen
        +__init__(screen)
        +inicio()
        +nivel_Dos()
        +nivel_Tres()
    }
    class Enemy {
        -caja
        -cubo
        -cube_size
        -pantalla_ancho
        -pantalla_alto
        -x
        -y
        -y_cubo
        -x_cubo
        -screen
        -jumpCount
        -direction
        -music
        +__init__(screen)
        +move()
        +draw_cube()
        +draw_box()
        +draw_all()
        +movecube()
        +colisiones(rect, jugador)
    }
    class Luna {
        -sheet
        -image
        -rect
        -frame
        -isJump
        -jumpCount
        -left_states
        -right_states
        -down_states
        -music
        -pantallaLuna
        -dead
        -size_cubo
        +__init__(position)
        +get_frame(frame_set)
        +clip(clipped_rect)
        +move(x)
        +update(direction)
        +handle_event(event)
        +jump()
    }
    class Music {
        -jump
        -fondo
        -golpe
        -muerte_sound
        +__init__()
        +saltar()
        +music_fondo()
        +colision()
        +muerte()
    }


'''
