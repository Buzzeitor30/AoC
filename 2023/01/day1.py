import re
import numpy as np

input_file = "input.txt"

part2_matches = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


with open(input_file) as file:
    data = file.readlines()


part1_parsed = [re.findall(rf"[0-9]", line.rstrip()) for line in data]
part1_sum = np.sum([int(x[0] + x[-1]) for x in part1_parsed])

part2_parsed = [re.findall(r'(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))', line.rstrip()) for line in data]
part2_sum = np.sum([int(part2_matches[x[0]] + part2_matches[x[-1]]) for x in part2_parsed])


print("Part 1 total sum is:", part1_sum)
print("Part 2 total sum is:", part2_sum)
