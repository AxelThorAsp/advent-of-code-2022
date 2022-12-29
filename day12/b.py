import sys  
from myheap import Node
from heapq import heappush, heappop

filepath = sys.argv[1]
fopen = open(filepath).readlines()
lines = map(lambda x: x.strip(), fopen)
visited = set()
M = [[] for _ in range(len(fopen))]
node_count = 0
i  = 0
for line in lines:
    for c in line:
        M[i].append(c)
    i += 1
R = len(M)
C = len(M[0])
adj = [[] for _ in range(R*C)]

starts=[]
def get_start():
    for i in range(R):
        for j in range(C):
            if M[i][j] == 'S' or M[i][j] == 'a':
                starts.append((i,j))

def num_to_coord(i):
    return (i // C, i % C)

def coord_to_num(i,j):
    return C * i + j

def ok(c, n):
    tempc = c 
    tempn = n 
    if tempc == 'S':
        tempc = 'a'
    if tempc == 'E':
        tempc = 'z'
    if tempn == 'E':
        tempn = 'z'
    if tempn == 'S':
        tempn = 'a'
    if (ord(tempn) < ord(tempc)) or (ord(tempc) + 1 == ord(tempn)) or tempn == tempc:
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

get_start()

for ss in starts:
    
    si, sj = ss

    nodes = [Node(i,9999) for i in range(R * C)]
    
    for n in nodes:
        for nbor in adj[n._id]:
            n.nbors.append(nodes[nbor])
    
    
    nodes[coord_to_num(si,sj)].dist=0
    prior = []
    heappush(prior,nodes[coord_to_num(si,sj)])
    done = []
    visited = set()
    while len(prior):
        curr = heappop(prior)
        visited.add(curr)
        for nbor in curr.nbors:
            if nbor not in visited:
                if nbor.dist > curr.dist + 1:
                    nbor.dist = curr.dist + 1
                    heappush(prior, nbor)
    
    d = {n._id : n for n in visited}
    
    def end():
        for i in range(R):
            for j in range(C):
                if M[i][j] == 'E':
                    return (i,j)

    try:
        print(d[coord_to_num(end()[0],end()[1])].dist)
    except KeyError:
        pass
