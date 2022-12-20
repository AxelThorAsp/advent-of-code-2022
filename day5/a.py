import sys
import re

WIDTH = 9
HEIGHT = 8

filepath = sys.argv[1]

class Stack:
    stack_ = []
    top = -1
    size = 0
    def __init__(self, size) -> None:
        self.size = size
        self.stack_ = [None for i in range(size)]

    def __repr__(self):
        return str(self.stack_)  

    def pop(self):
        if self.top == -1:
            return None
        ret = self.stack_[self.top]
        self.stack_[self.top] = None
        self.top -= 1
        return ret

    def push(self, item):
        if self.top + 1 == self.size:
            print("max stack size exceeded")
            return None
        self.top += 1
        self.stack_[self.top] = item

stacks = [Stack(128) for i in range(WIDTH)]


def parse_cargo(ops):
    for op in ops:
        for _ in op:
            c, i = _
            if c == ' ':
                continue
            stacks[i].push(c)
            
def helper(line):
    l = []
    for i in range(WIDTH):
        l.append((line[1 + 4*i], i))
    return l

def move(op):
    instruction = op.split()
    mv = int(instruction[1])
    frm = int(instruction[3]) - 1
    to = int(instruction[5]) - 1
    for i in range(mv):
        item = stacks[frm].pop()
        stacks[to].push(item)
        

def main():
    ops = []
    with open(filepath, 'r') as f:
        for i in range(HEIGHT):
            l = f.readline()
            ops.append(helper(l))
        ops.reverse()
        parse_cargo(ops)
        for line in f:
            if line.startswith("move"):
                move(line)
        for s in stacks:
            print(s.pop(), end='')
        print('')

if __name__ == "__main__":
    main()