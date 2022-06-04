import pygame
from classes.food_apple import FoodApple as Food
from classes.player import Snake

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRID_SIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRID_SIZE
GRID_HEIGHT = SCREEN_WIDTH / GRID_SIZE

# COLORS
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 0, 255)
COLOR_WHITE = (0, 0, 0)
BACKGROUND_COLOR_ONE = (93, 216, 228)
BACKGROUND_COLOR_TWO = (84, 194, 205)

# Game settings
GAME_SPEED = 10


def main():
    """
    This is our main game loop
    :return: void
    """
    # This is the order of setup IAW pygame documentation
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    # Setup the surface
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)
    # Initialize our player and a food
    # TODO Make this a function so we can add more settings especially when adding more foods
    snake = Snake()
    food = Food(COLOR_RED)

    my_font = pygame.font.SysFont("monospace", 16)

    while True:
        clock.tick(GAME_SPEED)  # This is where we would manipulate the speed slow/fast
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        # TODO Make this a function to track all types of objects that get added
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        # TODO Spawning function - to determine what's/how many spawned etc
        snake.draw(surface)
        food.draw(surface)

        screen.blit(surface, (0, 0))
        text = my_font.render(f"Score {snake.score}".format(snake.score), 1, COLOR_WHITE)
        screen.blit(text, (5, 10))
        pygame.display.update()


def drawGrid(surface):
    """
    We draw a grid based off our constant variables.
    Right now we are just saying for every other spot color the rect differently
    :param surface: This is the surface we draw to
    :return: void
    """
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, BACKGROUND_COLOR_ONE, rect)
            else:
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, BACKGROUND_COLOR_TWO, rect)


main()
