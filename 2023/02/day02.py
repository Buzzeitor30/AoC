import re
import numpy as np

MAX_RED = 12
MAX_BLUE = 14
MAX_GREEN = 13

with open("input.txt") as file:
    data = file.readlines()

game_id = 0
game_ids_part_1 = [game_id]
min_balls_part_2 = []

for game in data:
    game_id += 1
    red_balls = []
    blue_balls = []
    gren_balls = []
    min_red = 0
    min_blue = 0
    min_green = 0

    for n_balls, color in re.findall(r"(\d+)\s(blue|red|green)", game.rstrip()):
        if color == "red":
            red_balls.append(int(n_balls))
        elif color == "blue":
            blue_balls.append(int(n_balls))
        else:
            gren_balls.append(int(n_balls))
    min_balls_part_2.append(np.max(red_balls) * np.max(gren_balls) * np.max(blue_balls))
    if np.max(red_balls) > MAX_RED:
        continue
    if np.max(blue_balls) > MAX_BLUE:
        continue
    if np.max(gren_balls) > MAX_GREEN:
        continue
    game_ids_part_1.append(game_id)


print(np.sum(game_ids_part_1))
print(np.sum(min_balls_part_2))
