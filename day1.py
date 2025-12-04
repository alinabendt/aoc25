import math
# aoc25 day 1 part 1
position = 50
zero_count = 0

def dial(position, zero_count, direction, steps):
    if steps>100:
        steps = steps%100
    elif steps==100:
        steps = 0
    if direction=='L':  # left turns decrease
        position2 = position - steps
    else:  # right turns increase
        position2 = position + steps
    if position2>99:  # passing 99 as highest value
        position2 = position2%100  # 0 is also a position on the dial so need to use 100 instead of 99
    elif position2<0:  # passing 0 as lowest value
        position2 = 100-(abs(position2)%100)
    if position2 == 0:  # if the dial is at 0, count
        zero_count+=1
    return position2, zero_count

# part 2: also count passing zeros
def dial_passing(position, zero_count, direction, steps):
    if steps>100:
        zero_count+=math.floor(steps/100)
        steps = steps%100
    elif steps==100:
        steps = 0
        zero_count+=1
    if direction=='L':  # left turns decrease
        position2 = position - steps
        if position2==0:
            zero_count+=1
    else:  # right turns increase
        position2 = position + steps
    if position2>99:  # passing 99 as highest value
        position2 = position2%100  # 0 is also a position on the dial so need to use 100 instead of 99
        zero_count+=1
    elif position2<0:  # passing 0 as lowest value
        position2 = 100-(abs(position2)%100)
        if position!=0:
            zero_count+=1
    return position2, zero_count

with open("/home/solas/Documents/aoc_inputs/input1.txt", 'r') as file:
    for line in file:
        line = line.strip()
        direction = line[0]
        steps = [s for s in line if s.isdigit()]
        steps = "".join(map(str, steps))
        steps = int(steps)
        position, zero_count = dial_passing(position, zero_count, direction, steps)
print('password is: ', zero_count)
