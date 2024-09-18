import pygame
import pytiled-parser

# Initialize Pygame
pygame.init()

# Load the Tiled map using pytiled-parser
parser = pytiled-parser.TiledParser()
map_data = parser.parse_file('map.json')

# Define some constants
TILE_SIZE = map_data.tile_width
MAP_WIDTH = map_data.width
MAP_HEIGHT = map_data.height

# Create the game window
screen = pygame.display.set_mode((MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))

# Load the tileset
tileset = pygame.image.load('underwater.png')  # Replace with your tileset image
tileset_width, tileset_height = tileset.get_size()
tiles_per_row = tileset_width // TILE_SIZE

# Function to draw a tile
def draw_tile(tile_id, x, y):
    if tile_id == 0:
        return  # Don't draw empty tiles
    tile_x = (tile_id - 1) % tiles_per_row
    tile_y = (tile_id - 1) // tiles_per_row
    tile_rect = pygame.Rect(tile_x * TILE_SIZE, tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    screen.blit(tileset, (x, y), tile_rect)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the map
    screen.fill((0, 0, 0))  # Clear the screen
    for layer in map_data.layers:
        if isinstance(layer, pytiled-parser.TileLayer):
            for y, row in enumerate(layer.data):
                for x, tile_id in enumerate(row):
                    draw_tile(tile_id, x * TILE_SIZE, y * TILE_SIZE)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
