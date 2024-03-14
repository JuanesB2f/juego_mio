##DIAGRAMS

'''mermaid
sequenceDiagram
    participant pygame
    participant Music
    participant Nivel
    participant Enemy
    participant Luna

    Note over pygame, Music, Nivel, Enemy, Luna: Inicialización del juego

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
