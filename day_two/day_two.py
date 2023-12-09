import os

# Read data
with open(os.path.dirname(__file__) + '/day_two.txt', 'r') as f:
    data = f.read().splitlines()

# Part 1
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

# Part 2
result = 0
index = 0
for s in data:
    index += 1
    index_two = 2
    strings = s.split(" ")
    red = 0
    blue = 0
    green = 0
    while index_two < len(strings):
        if strings[index_two + 1][:3] == 'red':
            red = max(red, int(strings[index_two]))
        if strings[index_two + 1][:4] == 'blue':
            blue = max(blue, int(strings[index_two]))
        if strings[index_two + 1][:5] == 'green':
            green = max(green, int(strings[index_two]))
        index_two += 2
    result += red * blue * green

print(f'Result second part: {result}') # 63981