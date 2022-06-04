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
    draw_grid(surface)
    # Initialize our player and start with a food
    snake = Snake()
    food = Food(COLOR_RED)
    bad_food = Food(COLOR_GREEN)

    my_font = pygame.font.SysFont("monospace", 16)

    while True:
        clock.tick(GAME_SPEED)  # This is where we would manipulate the speed slow/fast
        snake.handle_keys()
        draw_grid(surface)
        snake.move()
        # TODO Make this a function to track all types of objects that get added
        if snake.get_head_position() == food.position:
            snake.length += food.length_value
            snake.score += food.point_value
            food.change_food()
            food.randomize_position()

        # We want to setup a function to determine what should or shouldn't be drawn to the screen.
        snake.draw(surface)
        food.draw(surface)

        screen.blit(surface, (0, 0))
        text = my_font.render(f"Score {snake.score}".format(snake.score), 1, COLOR_WHITE)
        screen.blit(text, (5, 10))
        pygame.display.update()


def draw_grid(surface):
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


def head_collision_detection(player_position, food, bad_food):
    """
    Due to the way our position tracking working at this time -
    :param player_position:
    :param food:
    :param bad_food:
    :return:
    """
    pass


# This is how the game starts
main()
