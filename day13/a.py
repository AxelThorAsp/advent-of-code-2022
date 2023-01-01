import sys 
filepath = sys.argv[1]
lines = [l.split('\n') for l in open(filepath).read().split('\n\n')]
c = 0
i = 0

def compare(a,b):
    if len(a) < len(b):
        a.append('stop')
    elif len(a) > len(b):
        b.append('stop')
    ops = list(map(lambda x, y: (x,y),a,b))
    for l,r in ops:
        match l, r:
            case int(), int():
                if l != r:
                    return l < r         
            case list(), list():
                ret = compare(l,r)
                if ret is not None:
                    return ret
            case int(), list():
                ret = compare([l],r)
                if ret is not None:
                    return ret 
            case list(), int():
                ret = compare(l,[r])
                if ret is not None:
                    return ret
            case _:
                if l == 'stop':
                    return True
                else:
                    return False

c = 0
for ll in lines:
    i += 1
    l = eval(ll[0])
    r = eval(ll[1])
    if compare(l,r):
        c += i 

print(c)