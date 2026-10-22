# Game of Thrones — Text Adventure

**Academic Project · SNHU · IT-140: Introduction to Scripting**

A Python-based text adventure inspired by the world of Westeros, featuring location-based exploration, inventory collection, and a final battle against the Night King.

**Play the Game:** [Try the interactive web version](https://www.tjordanart.com/got-text-game)

## Overview

Game of Thrones — Text Adventure is a command-line adventure game created for IT-140: Introduction to Scripting at Southern New Hampshire University.

Players explore locations throughout Westeros, collect six required items, and travel to Harrenhal for a final encounter with the Night King. The player's inventory determines whether they are prepared for the final battle.

The project applies Python fundamentals to a playable game, including functions, dictionaries, loops, conditional logic, user input, and game-state management.

## How to Play

The objective is to:

1. Explore locations throughout Westeros.
2. Collect all six required items.
3. Navigate to Harrenhal.
4. Face the Night King with the required items.

Arriving at Harrenhal without all six items results in defeat.

## Commands

**Movement**

```text
go North
go South
go East
go West
```

**Collect an item**

```text
get item
```

**Exit the game**

```text
exit
```

## Locations

Explore locations across Westeros and beyond:

- Winterfell
- King's Landing
- Riverrun
- The Eyrie
- Dragonstone
- Dorne
- Essos Port
- Harrenhal

## Items to Collect

Collect all six items before the final battle:

- Direwolf Pelt
- Raven Scroll
- Iron Throne Key
- Dragon Egg
- Sun Spear
- Poison Vial

## Game Mechanics

- **Location-based movement:** Navigate the game world using text commands.
- **Inventory management:** Collect and track required items.
- **Command processing:** Interpret player input to determine actions.
- **Game-state management:** Track progress toward the final encounter.
- **Win and lose conditions:** Determine the outcome based on inventory requirements.

## Technology

- **Python 3**
- **Dictionaries and data structures** — Represent locations and inventory
- **Functions** — Organize game behavior
- **Loops and conditional logic** — Control gameplay and evaluate player actions
- **User input** — Process commands and player decisions
- **Command-line interface** — Deliver the interactive experience

## How to Run Locally

**Requirements:** Python 3. No external dependencies.

Clone the repository:

```bash
git clone https://github.com/tjordanart/Game-of-Thrones-Text-Game-python-.git
```

Navigate to the project folder:

```bash
cd Game-of-Thrones-Text-Game-python-
```

Run the game:

```bash
python TextBasedGame-TJ.py
```

Follow the prompts to explore the world and collect the required items.

## Project Background

This
