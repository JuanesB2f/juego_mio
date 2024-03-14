##DIAGRAMS

'''mermaid
    Luna->>Music: music_fondo()
    Luna->>Nivel: inicio()
    loop Bucle Principal
        pygame->>Luna: handle_event(event)
        Luna->>Nivel: pantallaLuna
        Nivel-->>Luna: Nivel actual
        Luna->>Enemy: draw_all()
        Enemy->>Luna: colisiones(rect, jugador)
        Enemy->>Luna: movecube()
        Luna->>pygame: display.flip()
        pygame->>pygame: clock.tick(15)
    end
'''
