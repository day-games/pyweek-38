import pygame

from typing import NamedTuple, Any
import json
from pathlib import Path


class screen_size(NamedTuple):
    width: int
    height: int


def get_full_screen_size() -> screen_size:
    screen_info = pygame.display.Info()
    return screen_size(screen_info.current_w, screen_info.current_h)


def get_default_window_size() -> screen_size:
    return screen_size(640, 480)


def screen_sizes() -> "dict[str,dict[str,int]]":
    sizes: "dict[str, screen_size]" = {
        "DEFAULT_WINDOW_SIZE": get_default_window_size(),
        "FULL_SCREEN_SIZE": get_full_screen_size(),
    }

    return screen_sizes_to_dict(sizes)


def screen_sizes_to_dict(sizes: "dict[str, screen_size]") -> "dict[str,dict[str,int]]":
    op: dict[str, dict[str, int]] = {}
    for key, val in sizes.items():
        op[key] = {}
        op[key]["width"] = val.width
        op[key]["height"] = val.height
    return op


def serialize_sizes():
    with open("screen_sizes.json", "w") as f:
        json.dump(screen_sizes(), f)


def get_ser_sizes(filename: str="screen_sizes.json") -> "dict[str, screen_size]":
    screen_sizes_path = Path("screen_sizes.json")
    if not screen_sizes_path.is_file():
        raise Exception("delete screen_sizes.json if present and rerun the game.")
    with open(filename, "r") as f:
        return json.load(f)


def deser_sizes(sizes: "dict[str, Any]") -> "dict[str, screen_size]":
    return {key: screen_size(val["width"], val["height"]) for key, val in sizes.items()}


def set_global_window_sizes():
    screen_sizes_path = Path("screen_sizes.json")
    if not screen_sizes_path.is_file():
        raise Exception("delete screen_sizes.json if present and rerun the game.")
    sizes = deser_sizes(get_ser_sizes())
    for key, val in sizes.items():
        globals()[key] = val


def get_global_default_window_size() -> screen_size:
    return globals().get("DEFAULT_WINDOW_SIZE", get_default_window_size())


def get_global_full_screen_size() -> screen_size:
    return globals().get("FULL_SCREEN_SIZE", get_full_screen_size())
