import os

# Read data
with open(os.path.dirname(__file__) + '/day_one.txt', 'r') as f:
    data = f.read().splitlines()

# Part 1
result = 0
for i in range(len(data)):
    result += int(
        str(next((c for c in data[i] if c.isdigit()), ''))
        + str(next((c for c in data[i][::-1] if c.isdigit()), '')
    ))

print(f'Result first part: {result}') # 54239

# Part 2
NUMBER_CHAR = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

res = []
for value in data:
    temp_arr = [''] * len(value)
    
    for number in NUMBER_CHAR.keys():
        if value.find(number) != -1:
            temp_arr[value.find(number)] = NUMBER_CHAR[number]
        if value.rfind(number) != -1:
            temp_arr[value.rfind(number)] = NUMBER_CHAR[number]
    for i, char in enumerate(value):
        if char.isdigit():
            temp_arr[i] = char
    
    array = list(filter(None, temp_arr))
    answer = array[0] + array[-1]
    res.append(answer)

print(f'Result second part: {sum(int(value) for value in res)}') # 55343