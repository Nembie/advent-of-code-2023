# Advent of Code Day 1
# @autor:    Nembie
import os

result = 0
with open(os.path.dirname(__file__) + '/day_one.txt', 'r') as f:
    data = f.read().splitlines()
    for i in range(len(data)):
        result += int(
            str(next((c for c in data[i] if c.isdigit()), ''))
            + str(next((c for c in data[i][::-1] if c.isdigit()), '')
        ))

print(f'Result: {result}') # 54239