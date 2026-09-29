# Game Beatem-Up Side Scroller

A 2D beat-'em-up side-scroller built with Python and Pygame. Move through platform-based levels, attack enemies, manage health, and explore a scrolling game world.

## Requirements

- Python 3
- Pygame

Install Pygame with:

```bash
python -m pip install pygame
```

## Run

From the project directory, start the game with:

```bash
python main.py
```

## Controls

| Key | Action |
| --- | --- |
| `A` / `D` | Move left / right |
| `S` | Crouch |
| `Space` | Jump or wall jump |
| `O` | Attack |
| `O` + `A` / `D` | Dash left / right |
| `O` + `S` | Down attack / neutral down move |
| `J` | Take damage (debug control) |
| `B` | Load the next level |

Close the game window to exit.

## Project Structure

- `main.py` - Starts the Pygame game loop.
- `controller.py` - Handles input, level loading, updates, and rendering.
- `characters.py` - Player character movement, attacks, animation, and health.
- `structures.py` - Builds platforms and level structures from map data.
- `camera.py` - Follows the player through the level.
- `background.py` - Draws and moves the background.
- `inGameGUI.py` - Displays the in-game health bar and HUD.
- `maps/` - Level map data.
- `sprites/` - Game artwork and sprite sheets.
