from itertools import product
import re

def turn_on(x1, y1, x2, y2):
    for xy in product(range(x1,x2+1), range(y1,y2+1)):
        d[xy] = 1

def turn_on_brightness(x1, y1, x2, y2):
    for xy in product(range(x1,x2+1), range(y1,y2+1)):
        d[xy] += 1

def turn_off(x1, y1, x2, y2):
    for xy in product(range(x1,x2+1), range(y1,y2+1)):
        d[xy] = 0

def turn_off_brightness(x1, y1, x2, y2):
    for xy in product(range(x1,x2+1), range(y1,y2+1)):
        if d[xy] >= 1:
            d[xy] -= 1

def toggle(x1, y1, x2, y2):
    for xy in product(range(x1,x2+1), range(y1,y2+1)):
        if d[xy] == 0:
            d[xy] = 1
        else:
            d[xy] = 0

def toggle_brightness(x1, y1, x2, y2):
    for xy in product(range(x1,x2+1), range(y1,y2+1)):
        d[xy] += 2

d = dict()

for xy in product(range(0,1000), range(0,1000)):
    d[xy] = 0

with open('./inputs/6.txt', 'r') as instructions:
    for instruction in instructions:
        result = re.findall(r'[0-9]+,[0-9]+', instruction)
        x1, y1 = map(int, result[0].split(","))
        x2, y2 = map(int, result[1].split(","))
        if instruction.startswith("toggle"):
            #toggle(x1, y1, x2, y2)
            toggle_brightness(x1, y1, x2, y2)
        elif instruction.startswith("turn on"):
            #turn_on(x1, y1, x2, y2)
            turn_on_brightness(x1, y1, x2, y2)
        elif instruction.startswith("turn off"):
            #turn_off(x1, y1, x2, y2)
            turn_off_brightness(x1, y1, x2, y2)

print("Number on turned on lights: " + str(sum(d.values())))