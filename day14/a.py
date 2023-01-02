import sys 
from copy import deepcopy
import time
filepath = sys.argv[1]
lines = [l.split(' -> ') for l in open(filepath).read().split('\n')]
rocks = set()
maxy = 0 

for line in lines:
    ops = [list(map(int,_.split(','))) for _ in line]
    first = True
    last = None 
    lx,ly = None, None
    for cord in ops:
        x,y = cord
        rocks.add((x,y))
        maxy = max(maxy,y)
        if not first:
            if x == lx:
                put = min(y,ly)
                for _ in range(abs(y - ly) - 1):
                    rocks.add((x,put + 1))
                    put += 1
            elif y == ly:
                put = min(x,lx)
                for _ in range(abs(x-lx) - 1):
                    rocks.add((put + 1,y))
                    put += 1 
            else:
                assert False
        else:
            first = False
        last = (x,y)
        lx, ly = last

spawn = (500,0)
curr = (500,0)

def drop():
    fx,fy = spawn
    global rocks, curr 
    while True:
        if fy > maxy:
            return False
        curr = (fx,fy)
        if (fx,fy) in rocks:
            return False
        elif (fx,fy + 1) not in rocks:
            fy += 1 
        elif (fx - 1, fy + 1) not in rocks:
            fx -= 1
            fy += 1
        elif (fx + 1, fy + 1) not in rocks:
            fx += 1
            fy += 1 
        else:
            rocks.add((fx,fy))
            return True
def draw():
    global curr
    for r in range(10):
        for c in range(10):
            if (c+494,r) in rocks:
                print('#', end='')
            elif (c+494,r) == curr:
                print('+', end='')
            else:
                print('.', end='')
        print('')

i=0
while drop():
    i += 1

print(i)