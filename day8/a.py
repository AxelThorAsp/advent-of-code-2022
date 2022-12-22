import sys 

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

def check_tree(i, j, g, tree):
    if i == 0 or i == HI - 1:
        return True 
    if j == 0 or j == WI - 1:
        return True 
    #right
    if all(int(t) < tree for t in g[i][j + 1:]):
        return True
    #left
    if all(int(t) < tree for t in g[i][:j]):
        return True
    #down
    if all(int(t) < tree for t in [g[ii][j] for ii in range(i + 1, HI)]):
        return True 
    #up
    if all(int(t) < tree for t in [g[ii][j] for ii in range(i)]):
        return True

def count_visible(g):
    count = 0
    for i in range(HI):
        for j in range(WI):
            if check_tree(i, j, g, int(g[i][j])):
                count += 1
    return count

def main():
    print(count_visible(grid))

if __name__ == '__main__':
    main()
