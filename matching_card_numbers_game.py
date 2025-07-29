import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Playing with Cards - Memory Game")

ROWS, COLS = 4, 4
CARD_WIDTH = 100
CARD_HEIGHT = 140
MARGIN = 20

BG_COLOR = (30, 30, 30)
CARD_BACK_COLOR = (50, 50, 200)
CARD_FRONT_COLOR = (200, 200, 200)
TEXT_COLOR = (0, 0, 0)

font = pygame.font.SysFont("Arial", 48)


class Card:
    def __init__(self, value, x, y):
        self.value = value
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.is_flipped = False
        self.is_matched = False

    def draw(self, surface):
        if self.is_flipped or self.is_matched:
            pygame.draw.rect(surface, CARD_FRONT_COLOR, self.rect)
            text_surface = font.render(str(self.value), True, TEXT_COLOR)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)
        else:
            pygame.draw.rect(surface, CARD_BACK_COLOR, self.rect)


def create_cards():
    values = list(range(1, (ROWS * COLS // 2) + 1)) * 2
    random.shuffle(values)

    cards = []
    start_x = (WIDTH - (COLS * CARD_WIDTH + (COLS - 1) * MARGIN)) // 2
    start_y = (HEIGHT - (ROWS * CARD_HEIGHT + (ROWS - 1) * MARGIN)) // 2
    for row in range(ROWS):
        for col in range(COLS):
            x = start_x + col * (CARD_WIDTH + MARGIN)
            y = start_y + row * (CARD_HEIGHT + MARGIN)
            card = Card(values.pop(), x, y)
            cards.append(card)
    return cards


def draw_window(cards):
    WIN.fill(BG_COLOR)
    for card in cards:
        card.draw(WIN)
    pygame.display.update()


def main():
    cards = create_cards()
    selected_cards = []
    clock = pygame.time.Clock()
    running = True
    flip_back_delay = 1000

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for card in cards:
                    if card.rect.collidepoint(pos) and not card.is_flipped and not card.is_matched:
                        card.is_flipped = True
                        selected_cards.append(card)
                        if len(selected_cards) == 2:
                            if selected_cards[0].value != selected_cards[1].value:
                                draw_window(cards)
                                pygame.time.delay(flip_back_delay)
                                for c in selected_cards:
                                    c.is_flipped = False
                            else:
                                for c in selected_cards:
                                    c.is_matched = True
                            selected_cards = []
                        break

        draw_window(cards)

        if all(card.is_matched for card in cards):
            WIN.fill(BG_COLOR)
            win_text = font.render("You Won!", True, (255, 255, 255))
            win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            WIN.blit(win_text, win_rect)
            pygame.display.update()
            pygame.time.delay(3000)
            running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
