import sys

filepath = sys.argv[1]

ops = [d for d in map(lambda x: x.strip(), open(filepath).readlines())]

seen = set()
h = (0, 0)
t = (0, 0)

def man_dist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def move():
    global h,t
    hx, hy = h 
    tx, ty = t 
    if man_dist(h,t) <= 1:
        return
    elif hy == ty:
        assert man_dist(h,t) == 2 
        if hx > tx:
            t = (tx + 1, ty)
        else:
            t = (tx - 1, ty)
    elif hx == tx:
        assert man_dist(h,t) == 2 
        if hy > ty:
            t = (tx, ty + 1)
        else:
            t = (tx, ty - 1)

    elif man_dist(h,t) == 3:
        if hx > tx:
            if hy > ty:
                t = (tx + 1, ty + 1)
            else:
                t = (tx + 1, ty - 1)
        else:
            if hy > ty:
                t = (tx - 1, ty + 1)
            else:
                t = (tx - 1, ty - 1)
    else:
        assert man_dist(h,t) == 2



m = {
    'D' : (0, -1),
    'U' : (0, 1),
    'R' : (1, 0),
    'L' : (-1, 0)
}   

seen.add(t)

for op in ops:
    opp = op.split()
    _dir = opp[0]
    steps = opp[1]
    for _ in range(int(steps)):
        dx, dy = m[_dir]
        h = (h[0] + dx, h[1] + dy)
        move()
        seen.add(t)

print(len(seen))
print(h)