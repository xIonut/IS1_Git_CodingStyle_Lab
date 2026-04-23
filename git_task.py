import random
import pygame

# Constante pentru configurarea ferestrei și a grilei
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GRID_SIZE = 10
CELL_WIDTH = WINDOW_WIDTH // GRID_SIZE
CELL_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

def generate_color_grid():
    return [
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
         for _ in range(GRID_SIZE)] 
        for _ in range(GRID_SIZE)
    ]

def main():
    # Inițializarea modulelor Pygame
    pygame.init()

    # Configurarea ferestrei principale
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Procedural Color Grid (Regenerează la 5s sau la apăsarea SPACE)")

    # Generarea inițială a grilei de culori
    grid_colors = generate_color_grid()

    # Crearea unui eveniment personalizat pentru regenerarea la 5 secunde (5000 ms)
    REGENERATE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(REGENERATE_EVENT, 5000)

    # Variabilă de control pentru bucla principală
    running = True

    # Bucla principală a aplicației
    while running:
        # Umplerea fundalului cu negru
        screen.fill((0, 0, 0))

        # Desenarea grilei de culori
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                color = grid_colors[row][col]
                x_pos = col * CELL_WIDTH
                y_pos = row * CELL_HEIGHT
                
                # Desenarea fiecărui pătrat (celulă)
                pygame.draw.rect(screen, color, (x_pos, y_pos, CELL_WIDTH, CELL_HEIGHT))

        # Actualizarea ecranului
        pygame.display.flip()

        # Gestionarea evenimentelor
        for event in pygame.event.get():
            # Verificăm dacă utilizatorul a apăsat pe butonul de închidere [X]
            if event.type == pygame.QUIT:
                running = False
            
            # Verificăm dacă a fost apăsată o tastă
            elif event.type == pygame.KEYDOWN:
                # La apăsarea tastei SPACE, regenerăm grila manual
                if event.key == pygame.K_SPACE:
                    grid_colors = generate_color_grid()
                    # Resetăm timer-ul pentru a evita regenerarea automată imediat după cea manuală
                    pygame.time.set_timer(REGENERATE_EVENT, 5000)

            # Verificăm dacă a expirat timer-ul de 5 secunde
            elif event.type == REGENERATE_EVENT:
                grid_colors = generate_color_grid()

    # Închiderea corectă a aplicației Pygame
    pygame.quit()

# Punctul de intrare în program
if __name__ == "__main__":
    main()