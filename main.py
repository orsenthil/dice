"""Simulate a six-sided dice roll.

Usage:

$ python dice.py
How many dice do you want to roll? [1-6] 5

~~~~~~~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~~~~~~~
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│  ●   ●  │ │  ●      │ │  ●   ●  │ │  ●   ●  │ │         │
│    ●    │ │         │ │    ●    │ │    ●    │ │    ●    │
│  ●   ●  │ │      ●  │ │  ●   ●  │ │  ●   ●  │ │         │
└─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
"""

import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def parse_input(input_string):
    if input_string.isdigit():
        if 1 <= int(input_string) <= 6:
            return int(input_string)
    else:
        print("Invalid input. Please enter a number between 1 and 6.")
        raise SystemExit(1)

def roll_dice(num_dice):
    """Return a list of `num_dice` dice rolls."""
    return [random.randint(1, 6) for _ in range(num_dice)]


def _get_dice_faces(dice_values):
    return [DICE_ART[die] for die in dice_values]

def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for dice in dice_faces:
            row_components.append(dice[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows

def generate_dice_faces_diagram(dice_values):
    """Return an ASCII diagram of dice faces from `dice_values`."""

    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


if __name__ == "__main__":
    num_dice = parse_input(input("How many dice do you want to roll? [1-6] "))
    dice_values = roll_dice(num_dice)
    print(f"\n{generate_dice_faces_diagram(dice_values)}")