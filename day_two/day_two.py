import os

# Part 1
with open(os.path.dirname(__file__) + '/day_two.txt', 'r') as f:
    data = f.read().splitlines()

result = 0
index = 0
for value in data:
    index += 1
    index_two = 2
    checker = True
    strings = value.split(" ")
    while index_two < len(strings):
        if (
            (strings[index_two + 1][0] == 'r' and int(strings[index_two]) > 12)
            or (strings[index_two + 1][0] == 'g' and int(strings[index_two]) > 13)
            or (strings[index_two + 1][0] == 'b' and int(strings[index_two]) > 14)
        ):
            checker = False
        index_two += 2
    if checker:
        result += index

print(f'Result first part: {result}') # 2449