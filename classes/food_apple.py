from random import randint

from food import Food

# Temporary example of how it can be done
FOOD_TYPES = [
    {
        'length': 1,
        'score': 1,
        'color': (255, 153, 153),
    },
    {
        'length': 2,
        'score': 1,
        'color': (255, 178, 102),
    },
    {
        'length': 1,
        'score': 2,
        'color': (255, 255, 204),
    },
    {
        'length': 0,
        'score': 3,
        'color': (255, 255, 0),
    },
    {
        'length': 3,
        'score': 0,
        'color': (204, 0, 102),
    },
]


class FoodApple(Food):
    def __init__(self, color):
        Food.__init__(self, color)
        self.point_value = 1
        self.length_value = 1

    def adjust_point_value(self, value):
        self.point_value = value

    def adjust_length_value(self, value):
        self.length_value = value

    def adjust_color(self, new_color):
        self.color = new_color

    def change_food(self):
        # This is the basics of what could be advanced logic for determining what the next food type will be instead
        # of just a random roll on the list
        food_type = FOOD_TYPES[randint(0, len(FOOD_TYPES) - 1)]
        self.length_value = food_type['length']
        self.point_value = food_type['score']
        self.color = food_type['color']
