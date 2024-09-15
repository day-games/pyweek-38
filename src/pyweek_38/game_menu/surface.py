import pygame
import sys
from typing import Tuple

PYGAME_ICON = [None]

def create_basic_surface(
    title: str = "pygame-38 default title",
    surface: pygame.Surface = None,
    window_size: Tuple[int, int] = None,
    pygame_menu_icon: bool = True,
    init_pygame: bool = False,
    center_window: bool = False,
    **kwargs,
) -> pygame.Surface:
    if init_pygame:
        pygame.init()
    if center_window:
        import os
        os.environ["SDL_VIDEO_CENTERED"] = "1"
    if surface is None and window_size is not None:
        surface = pygame.display.set_mode(window_size, **kwargs)
    pygame.display.set_caption(title)
    if pygame_menu_icon:
        try:
            if PYGAME_ICON[0] is None:
                from pygame_menu.baseimage import IMAGE_EXAMPLE_PYGAME_MENU, BaseImage
                icon = BaseImage(IMAGE_EXAMPLE_PYGAME_MENU).get_surface(new=False)
                pygame.display.set_icon(icon)
                PYGAME_ICON[0] = icon
            else:
                pygame.display.set_icon(PYGAME_ICON[0])
        except:
            pass
    return surface
