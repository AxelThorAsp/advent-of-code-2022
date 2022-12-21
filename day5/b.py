import sys

WIDTH = 9 
HEIGHT = 8

filepath = sys.argv[1]

class Column:
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
    

    def slice(self, cnt):
        ret = self.stack_[self.top + 1 - cnt:self.top + 1]
        self.top = self.top - cnt
        return ret

    def add(self, sub):
        self.top += 1
        for i, c  in enumerate(sub):
            self.stack_[self.top] = c
            self.top += 1
        self.top -= 1

columns = [Column(126) for i in range(WIDTH)]


def parse_cargo(ops):
    for op in ops:
        for _ in op:
            c, i = _
            if c == ' ':
                continue
            columns[i].push(c)
            
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
    temp = columns[frm].slice(mv)
    columns[to].add(temp)
        

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
        for s in columns:
            print(s.pop(), end='')
        print('')

if __name__ == "__main__":
    main()
