# aoc25 day 1 part 1
position = 50
zero_count = 0

def dial(position, zero_count, direction, steps):
    if direction=='L':
        position -= steps
    else:
        position += steps
    if position>99:
        position = position%99
    elif position<0:
        position = 99+position
    elif position == 0:
        zero_count+=1
    return position, zero_count

with open("C:/Users/solas/Documents/GitHub/aoc25/input1.txt", 'r') as file:
    for line in file:
        line = line.strip()
        direction = line[0]
        print(direction)
        steps = [s for s in line if s.isdigit()]
        steps = steps[0]+steps[1]
        steps = int(steps)
        position, zero_count = dial(position, zero_count, direction, steps)
print(zero_count)