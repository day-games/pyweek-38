import pygame
import pygame_menu
from pygame.locals import RESIZABLE
from typing import Tuple, Any, Callable
from .surface import create_basic_surface
from src.pyweek_38.util.window_util import screen_size, get_global_default_window_size, get_global_full_screen_size

def generate_surface(title: str, surface: pygame.Surface) -> pygame.Surface:
    return create_basic_surface(title, surface, center_window=True)

def set_window_size(selected: Tuple, menu: pygame_menu.Menu, value: Callable[[], screen_size]) -> None:
    window_size = value()
    pygame.display.set_mode(window_size, RESIZABLE)
    width, height = pygame.display.get_window_size()
    menu.resize(width=width, height=height)

def set_difficulty(selected: Tuple, value: Any) -> None:
    print(f"Set difficulty to {selected[0]} ({value})")

def start_the_game() -> None:
    user_name = globals().get("USER_NAME")
    if user_name:
        print(f"{user_name.get_value()}, Do the job here!")

def create_menu(window_size: screen_size):
    menu = pygame_menu.Menu(
        theme=pygame_menu.themes.THEME_BLUE,
        title="Welcome",
        height=window_size.height,
        width=window_size.width,
    )

    user_name = menu.add.text_input("Name: ", default="John Doe", maxchar=10)
    globals()["USER_NAME"] = user_name

    menu.add.selector("Difficulty: ", [("Hard", 1), ("Easy", 2)], onchange=set_difficulty)
    menu.add.button("Play", start_the_game)
    menu.add.button("Quit", pygame_menu.events.EXIT)
    menu.add.selector(
        "Screen Size: ",
        [
            ("default", menu, get_global_default_window_size),
            ("full screen", menu, get_global_full_screen_size),
        ],
        onchange=set_window_size,
    )
    return menu

def run_in_menu(menu: pygame_menu.Menu, screen: Any):
    menu.mainloop(screen)

def run_main_menu(surface: pygame.Surface):
    width, height = surface.get_size()
    run_in_menu(create_menu(screen_size(width, height)), generate_surface("pyweek-38", surface))
