import sys
from itertools import takewhile 
from functools import reduce 
from operator import mul

filepath = sys.argv[1]


def parse(fp):
    grid = [l for l in 
            map(lambda x: x.strip(), open(fp).readlines())
        ]
    return grid

grid = parse(filepath)

def measure(g):
    return (len(g), len(g[0]))

HI, WI = measure(grid)

def count(line, tree):
    c = 0
    for i in range(len(line)):
        if int(line[i]) >= tree:
            return c + 1
        else:
            c += 1
    return c


def check_tree(i, j, g, tree):
    
    trees = []

    if i == 0 or i == HI - 1:
        return [] 
    if j == 0 or j == WI - 1:
        return [] 
    
    #right 
    trees.append(count([t for t in g[i][j + 1:]], tree))
        
    #left
    trees.append(count([t for t in g[i][:j][::-1]], tree))
        
    #down
    trees.append(count([t for t in [g[ii][j] for ii in range(i + 1, HI)]], tree)) 
    #up
    trees.append(count([t for t in [g[ii][j] for ii in range(i)]][::-1], tree))
    return trees

def mul_sum(l):
    return reduce(mul, l)


def scenic_score(g):
    maxseen = float('-inf')
    for i in range(HI):
        for j in range(WI):
            out = check_tree(i, j, g, int(g[i][j]))
            if not out:
                continue
            else:
                maxseen = max(maxseen,mul_sum(out))
    return maxseen

def main():
    print(scenic_score(grid))

if __name__ == '__main__':
    main()
