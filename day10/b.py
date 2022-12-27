
import sys 

filepath = sys.argv[1]

ops = map(lambda x: x.split(),open(filepath).readlines())

display = [['.' for i in range(40)] for j  in range(6)]


reg = 1
cycle = 1

def show_display():
    for j in range(6):
        for i in range(40):
            print(display[j][i], end= "")
        print("")

def draw(c):
    row = c // 40
    col = c % 40
    display[row][col] = '#'

def check():
    if ((cycle - 1) % 40) in range(reg - 1, reg + 2):
        draw(cycle - 1)

for op in ops:
    if op[0] == 'noop':
        check()
        cycle += 1
    
    elif op[0] == 'addx':
        check()
        cycle += 1
        check()
        cycle += 1
        reg += int(op[1])
    else:
        assert False, 'unreachable'

show_display()