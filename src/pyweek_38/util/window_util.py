import pygame
import json
from pathlib import Path
from typing import NamedTuple, Dict, Any

class screen_size(NamedTuple):
    width: int
    height: int

def get_full_screen_size() -> screen_size:
    screen_info = pygame.display.Info()
    return screen_size(screen_info.current_w, screen_info.current_h)

def get_default_window_size() -> screen_size:
    return screen_size(640, 480)

def screen_sizes() -> Dict[str, Dict[str, int]]:
    sizes = {
        "DEFAULT_WINDOW_SIZE": get_default_window_size(),
        "FULL_SCREEN_SIZE": get_full_screen_size(),
    }
    return {key: {"width": val.width, "height": val.height} for key, val in sizes.items()}

def serialize_sizes():
    with open("screen_sizes.json", "w") as f:
        json.dump(screen_sizes(), f)

def get_ser_sizes(filename: str = "screen_sizes.json") -> Dict[str, Any]:
    screen_sizes_path = Path(filename)
    if not screen_sizes_path.is_file():
        raise FileNotFoundError(f"{filename} not found. Please run the game to generate it.")
    with open(filename, "r") as f:
        return json.load(f)

def deser_sizes(sizes: Dict[str, Any]) -> Dict[str, screen_size]:
    return {key: screen_size(val["width"], val["height"]) for key, val in sizes.items()}

def set_global_window_sizes():
    sizes = deser_sizes(get_ser_sizes())
    globals().update(sizes)

def get_global_default_window_size() -> screen_size:
    return globals().get("DEFAULT_WINDOW_SIZE", get_default_window_size())

def get_global_full_screen_size() -> screen_size:
    return globals().get("FULL_SCREEN_SIZE", get_full_screen_size())
