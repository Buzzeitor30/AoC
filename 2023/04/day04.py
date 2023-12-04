import re
import numpy as np

with open("input.txt") as file:
    data = file.readlines()


def calculate_points(n):
    if n == 0:
        return 0
    return 2 ** (n - 1)


points = []

scratch_cards = [1] * len(data)
i = 0
for line in data:
    parsed_line = re.sub(r"Card\s+\d+:", " ", line.rstrip())
    winning_numbers, numbers = parsed_line.split("|")
    winning_numbers = set(filter(None, winning_numbers.split(" ")))
    numbers = set(filter(None, numbers.split(" ")))

    total_correct = winning_numbers & numbers
    points.append(calculate_points((len(total_correct))))

    for j in range(i + 1, i + 1 + len(total_correct)):
        scratch_cards[j] += 1 * scratch_cards[i]
    i += 1

print("Total points is:", np.sum(points))
print("Total of scratch cards is:", np.sum(scratch_cards))
