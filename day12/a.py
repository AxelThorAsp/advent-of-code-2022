import sys  
from myheap import myHeap

filepath = sys.argv[1]
lines = map(lambda x: x.strip(), open(filepath).readlines())
visited = set()
M = [[] for _ in range(5)]
node_count = 0
i  = 0
for line in lines:
    for c in line:
        M[i].append(c)
    i += 1
R = len(M)
C = len(M[0])
adj = [[] for i in range(R*C)]

def num_to_coord(i):
    return (i // C, i % C)

def coord_to_num(i,j):
    return C * i + j

def ok(c, n):
    if c == 'S' or c == 'E':
        return True
    if n == 'S' or n == 'E':
        return True 
    if (ord(n) < ord(c)) or (ord(c) + 1 == ord(n)) or n == c:
        return True  
    return False

def check_dirs(i,j):
    c = M[i][j]
    global node_count
    if i != 0:
        #move up
        if ok(c,M[i-1][j]):
            adj[node_count].append(coord_to_num(i-1,j))
    if i != R - 1:
        #move down
        if ok(c,M[i + 1][j]):
            adj[node_count].append(coord_to_num(i+1,j))
    if j != 0:
        #move left
        if ok(c, M[i][j - 1]):
            adj[node_count].append(coord_to_num(i,j-1))
    if j != C - 1:
        #move right
        if ok(c, M[i][j + 1]):
            adj[node_count].append(coord_to_num(i,j+1))
    node_count += 1

for i in range(R):
    for j in range(C):
        check_dirs(i,j)

pq = myHeap()

for n in range(R * C):
    pq.add_task(n, 99999)

pq.add_task(0,0)

for n in range(R * C):
    for _n in adj[n]:
        pq.add_task((_n, n))