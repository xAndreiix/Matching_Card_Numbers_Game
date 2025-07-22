# Matching Card Numbers Game (Memory Game)

This is a classic memory-based matching card game developed with Python and Pygame. The game challenges players to find matching card pairs by remembering card positions. It offers a clean graphical interface and responsive interaction mechanics.

## Features

- 4x4 grid with randomized card positions.
- Flip, match, and win logic implemented.
- Visual card flipping using rectangles and text.
- Smooth user experience with animations and win message.

## Requirements

- Python 3.7+
- [pygame](https://pypi.org/project/pygame/)

### Install dependencies

```bash```
pip install pygame

## Files
- matching_card_numbers_game.py — Main Pygame game logic.
- test_matching_card_numbers_game.py — Unit tests for core card behavior.
- .gitignore — Excludes IDE, system, and Python cache files.
- README.md — Project documentation.
- LICENSE — Licensing details (MIT).

## Running the Game
python matching_card_numbers_game.py
Click two cards to reveal their values. If they match, they stay flipped. Win when all pairs are found.

## Running Tests
python test_matching_card_numbers_game.py