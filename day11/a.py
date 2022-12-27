
import sys 
import operator
filepath = sys.argv[1]

d = {
    '+': operator.add,
    '*': operator.mul,
}

class Monkey:
    def __init__(self):
        self.starting = []
        self.op = None
        self.test = None
        self.tru = None 
        self.fals = None
        self.insp = 0

    def catch(self, item):
        self.starting.append(item)

    def yeet(self):
        item = self.starting.pop(0)
        item = self.op(item)
        item = item // 3
        return item

    def __repr__(self):
        return f"""
        starting = {self.starting}
        op = {self.op(1)}
        test = {self.test}
        tru = {self.tru}
        fals = {self.fals}
        inspections = {self.insp}
        """

monkeys = [Monkey() for _ in range(8)]
i = -1

def makefunc(_opp, n):
    def f(x):
        if n == 'old':
            return d[_opp](x,x)
        else:
            return d[_opp](x,int(n))
    return f 

ops = open(filepath).read().split('\n\n')

for opp in ops:
    for operation in map(lambda x: x.strip(), opp.replace(',', '').split('\n')):
        if operation.startswith("Monkey"):
            i += 1
        elif operation.startswith("Starting"):
            for n in operation.split():
                if n.isnumeric():
                    monkeys[i].starting.append(int(n))
        elif operation.startswith("Operation"):
            _ = operation.split()
            monkeys[i].op = makefunc(_[-2], _[-1])
        elif operation.startswith("Test"):
            monkeys[i].test = int(operation.split()[-1])
        elif operation.startswith("If true"):
            monkeys[i].tru = int(operation.split()[-1])
        elif operation.startswith("If false"):
            monkeys[i].fals = int(operation.split()[-1])
for _ in range(20):
    for m in monkeys:
        for i in range(len(m.starting)):
            m.insp += 1
            item = m.yeet()
            if (item % m.test) == 0:
                monkeys[m.tru].catch(item)
            else:
                monkeys[m.fals].catch(item)

print(sorted([m.insp for m in monkeys]))