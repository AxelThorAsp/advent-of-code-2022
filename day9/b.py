import sys

filepath = sys.argv[1]

ops = [d for d in map(lambda x: x.strip(), open(filepath).readlines())]

seen = set()

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return f"({self.x},{self.y})"

snake = [Coord(0,0) for _ in range(10)]

def man_dist(a: Coord , b: Coord):
    return abs(a.x - b.x) + abs(a.y - b.y)

def move(h,t):
    global snake
    hx, hy = (h.x, h.y) 
    tx, ty = (t.x, t.y)

    if man_dist(h,t) <= 1:
        return
    elif hy == ty:
        assert man_dist(h,t) == 2 
        if hx > tx:
            t.x += 1
        else:
            t.x -= 1
    elif hx == tx:
        assert man_dist(h,t) == 2 
        if hy > ty:
            t.y += 1
        else:
            t.y -= 1

    elif man_dist(h,t) == 3:
        if hx > tx:
            if hy > ty:
                t.x += 1 
                t.y += 1
            else:
                t.x += 1
                t.y -= 1
        else:
            if hy > ty:
                t.x -=1 
                t.y += 1
            else:    
                t.x -= 1
                t.y -= 1
    
    elif man_dist(h,t) == 4:
        if hx > tx:
            if hy > ty:
                t.x += 1
                t.y += 1
            else:
                t.x += 1
                t.y -= 1
        else:
            if hy > ty:
                t.x -= 1 
                t.y += 1
            else:
                t.x -= 1
                t.y -= 1
    else:
        pass
        



def print_board():
    for i in range(12, -1,-1):
        for j in range(12):
            found = False
            for s in snake:
                if s.x == j and s.y == i:
                    print("*", end = "")
                    found = True
                    break
            if not found:
                print("s", end = '')
        print("")
                

m = {
    'D' : (0, -1),
    'U' : (0, 1),
    'R' : (1, 0),
    'L' : (-1, 0)
}   

seen.add((snake[9].x,snake[9].y))

for op in ops:
    opp = op.split()
    _dir = opp[0]
    steps = opp[1]
    for _ in range(int(steps)):
        dx, dy = m[_dir]
        snake[0].x += dx 
        snake[0].y += dy 
        for i in range(9):
            move(snake[i], snake[i+1])
        seen.add((snake[9].x, snake[9].y))


#print_board()
print(len(seen))
#print(snake)