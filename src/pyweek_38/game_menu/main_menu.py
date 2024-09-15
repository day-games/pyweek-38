"""
pygame-menu
https://github.com/ppizarror/pygame-menu

EXAMPLE - SIMPLE
Super simple example of pygame-menu usage, featuring a selector and a button.
"""

import pygame
from pygame.locals import RESIZABLE
from pygame import Surface
import pygame_menu

from .surface import create_basic_surface
from typing import Tuple, Any, Callable
from src.pyweek_38.util.window_util import (
    screen_size,
    get_global_default_window_size,
    get_global_full_screen_size,
)


def generate_surface(title: str, surface: Surface) -> Surface:
    return create_basic_surface(title, surface, center_window=True)


def set_window_size(
    selected: Tuple, menu: pygame_menu.Menu, value: Callable[[], screen_size]
) -> None:
    print(selected, "menu: ", menu, "val type:", type(value))
    window_size = value()
    print(window_size)
    pygame.display.set_mode(window_size, RESIZABLE)
    width, height = pygame.display.get_window_size()
    menu.resize(width=width, height=height)


def set_difficulty(selected: Tuple, value: Any) -> None:
    """
    Set the difficulty of the game.
    """
    print(f"Set difficulty to {selected[0]} ({value})")


def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    user_name = globals()["USER_NAME"]
    print(f"{user_name.get_value()}, Do the job here!")


def create_menu(window_size: screen_size):
    """
    This function creates the menu for the game.
    It will include a text input for user's name, a selector for difficulty,
    a button to start the game and a button to quit the game.
    """

    # Create a new menu object with the given dimensions, theme and title
    menu = pygame_menu.Menu(
        theme=pygame_menu.themes.THEME_BLUE,  # Theme of the menu
        title="Welcome",  # Title of the menu
        height=window_size.height,  # Height of the menu in pixels
        width=window_size.width,  # Width of the menu in pixels
    )

    # flake8: noqa
    # Add a text input for the user's name
    user_name = menu.add.text_input(
        "Name: ",  # Label for the input field
        default="John Doe",  # Default value for the input field
        maxchar=10,  # Maximum number of characters allowed in the input field
    )
    globals()["USER_NAME"] = user_name

    # Add a selector for difficulty
    menu.add.selector(
        "Difficulty: ",  # Label for the selector
        [("Hard", 1), ("Easy", 2)],  # Options for the selector
        onchange=set_difficulty,  # Function to handle change
    )
    # Add a button to start the game
    menu.add.button("Play", start_the_game)

    # Add a button to quit the game
    menu.add.button("Quit", pygame_menu.events.EXIT)

    # Add a selector for screen size
    menu.add.selector(
        "Screen Size: ",  # Label for the selector
        [
            ("default", menu, get_global_default_window_size),
            ("full screen", menu, get_global_full_screen_size),
        ],  # Options for the selector
        onchange=set_window_size,  # Function to handle change
    )
    # Return the created menu
    return menu


def run_in_menu(menu: "pygame_menu.Menu", screen: "Any"):
    """
    Run the main loop of the given menu on the specified surface.
    """
    menu.mainloop(screen)


def run_main_menu(surface: Surface):
    """
    Run the main menu by creating it and passing it to the main loop function.

    This function is responsible for launching the main menu of the game.
    It creates the menu, sets the surface it will be displayed on,
    and runs the main loop.
    """
    width, height = surface.get_size()
    run_in_menu(
        create_menu(screen_size(width, height)), generate_surface("pyweek-38", surface)
    )
