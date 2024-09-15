from src.pyweek_38.game_menu.main_menu import run_main_menu
from src.pyweek_38.util.window_util import (
    get_global_full_screen_size,
    screen_sizes,
    serialize_sizes,
    set_global_window_sizes,
)
import pygame
from pygame.locals import RESIZABLE

pygame.init()
print(screen_sizes())

serialize_sizes()
set_global_window_sizes()
print(globals())
surface: pygame.Surface = pygame.display.set_mode(get_global_full_screen_size(), RESIZABLE)


if __name__ == "__main__":
    run_main_menu(surface)


