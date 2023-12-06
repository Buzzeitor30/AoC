import re
import numpy as np

def solve_quadatric_equation(a, b, c):
    x1 = (-b + np.sqrt(b ** 2 - 4*a*c)) / 2 * a
    x2 = (-b - np.sqrt(b ** 2 - 4*a*c)) / 2 * a
    return x1, x2


with open("input.txt") as f:
    data = [re.findall(r'\d+', line.rstrip()) for line in f.readlines()]


#The problem can be seen as solving inequation distance < button_down*(total_time - button_down)
# i.e a = -1, b=total_time, c=distance
a = -1 #constant
number_of_ways_per_race = []
for race in range(0, len(data[0])):
    b, c = int(data[0][race]), -int(data[1][race])
    x1, x2 = solve_quadatric_equation(a, b, c)
    number_of_ways_per_race.append(np.ceil(x2) - np.floor(x1) - 1)
#Part 2 for a single race
b = int(''.join(data[0]))
c =  -int(''.join(data[1]))
x1, x2 = solve_quadatric_equation(a, b, c)
number_of_ways_single_race = np.ceil(x2) - np.floor(x1) - 1


print("Number of total ways to beat all the races is:", np.prod(number_of_ways_per_race))
print("Number of ways to win the single race", number_of_ways_single_race)