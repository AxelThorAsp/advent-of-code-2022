
import sys 

filepath = sys.argv[1]

ops = map(lambda x: x.split(),open(filepath).readlines())

reg = 1
cycle = 1
signal_strength = 0


def check():
    targ = [20,60,100,140,180,220]
    global signal_strength
    if cycle in targ:
        print(reg, "Cycle: ", end=  "")
        print(cycle)
        signal_strength += cycle * reg
    else:
        return 

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

print(signal_strength)