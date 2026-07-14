# SNAKE - nasza gra!
# Kod dziala, ale cos tu jest mocno popsute...
# Wykonuj zadania z kartki po kolei. Szukaj komentarzy: ZADANIE 1, ZADANIE 2...
# Po kazdym zadaniu zapisz plik (Ctrl+S) i uruchom gre przyciskiem Run.

import pygame
import random

CELL = 25          # rozmiar jednej kratki w pikselach
COLS = 24          # ile kratek w poziomie
ROWS = 18          # ile kratek w pionie

pygame.init()
screen = pygame.display.set_mode((COLS * CELL, ROWS * CELL))

# ZADANIE 1: Nadaj grze wlasny tytul!
pygame.display.set_caption("wonsz rzeczny")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Waz to lista kratek (x, y). Pierwsza kratka to glowa.
snake = [(5, 9), (4, 9), (3, 9)]
dx, dy = 1, 0                      # kierunek ruchu: w prawo
apple = (15, 9)
score = 0
running = True

while running:

    # --- 1. KLAWIATURA ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # ZADANIE 6: Dziala tylko strzalka w gore! Dopisz trzy pozostale.
            if event.key == pygame.K_UP and dy != 1:
                dx, dy = 0, -1

    # --- 2. RUCH WEZA ---
    head = (snake[0][0] + dx, snake[0][1] + dy)   # nowa glowa
    snake.insert(0, head)                          # doklejamy ja z przodu

    # ZADANIE 7: Waz nie umie zjesc jablka! Napraw warunek
    # i napisz, co ma sie stac po zjedzeniu.
    if False:
        pass   # <-- to slowo skasuj i pisz tutaj
    else:
        snake.pop()      # nie zjadl - usuwamy ogon, zeby waz nie rosl

    # ZADANIE 8: Waz ucieka poza ekran i nic sie nie dzieje!
    # Dopisz warunek konca gry po uderzeniu w sciane.
    x, y = head

    # --- 3. RYSOWANIE ---
    # ZADANIE 2: Kto wybral ten okropny kolor tla?! Zmien go.
    screen.fill((255, 0, 255))

    # jablko
    ax, ay = apple
    pygame.draw.circle(screen, (220, 40, 40),
                       (ax * CELL + CELL // 2, ay * CELL + CELL // 2),
                       CELL // 2)

    # waz - rysujemy kazda kratke z listy
    # ZADANIE 3: Gdzie jest waz?! Ta petla wykonuje sie ZERO razy...
    for i in range(0, 0):
        x, y = snake[i]
        # ZADANIE 4: Waz jest chudy jak okruszek. Kratka ma rozmiar CELL.
        pygame.draw.rect(screen, (90, 200, 70),
                         (x * CELL, y * CELL, 4, 4))

    # ZADANIE 9: Licznik klamie! Zawsze pokazuje zero...
    text = font.render("Punkty: 0", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

    # ZADANIE 5: Ten waz to chyba slimak. Przyspiesz go!
    # (liczba = ile krokow na sekunde robi waz)
    clock.tick(2)

# --- KONIEC GRY ---
screen.fill((0, 0, 0))
text = font.render("KONIEC GRY! Punkty: " + str(score), True, (255, 255, 255))
screen.blit(text, (140, 200))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
