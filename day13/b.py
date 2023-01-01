import sys 
from copy import deepcopy
from functools import total_ordering
filepath = sys.argv[1]
lines = [l.split('\n') for l in open(filepath).read().split('\n\n')]
c = 0
i = 0

def compare(a,b):
    aa = deepcopy(a)
    bb = deepcopy(b)
    if len(aa) < len(bb):
        aa.append('stop')
    elif len(aa) > len(bb):
        bb.append('stop')
    ops = list(map(lambda x, y: (x,y),aa,bb))
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
@total_ordering
class Packet:
    def __init__(self, p: list) -> None:
        self.packet = p
    def __eq__(self, __o: object) -> bool:
        if self is __o:
            return True
        if isinstance(__o, Packet):
            return compare(self.packet, __o.packet) is None
        return False 
    def __lt__(self, __o: object) -> bool:
        if isinstance(__o, Packet):
            if compare(self.packet, __o.packet):
                return True
            return False
        return False
    def __repr__(self) -> str:
        return str(self.packet)
    
c = 0
packs = []
p1 = Packet([[2]])
p2 = Packet([[6]])
for ll in lines:
    i += 1
    l = eval(ll[0])
    r = eval(ll[1])
    packs.extend([Packet(l),Packet(r)])

packs.extend([p1,p2])

pp = 1
packs.sort()
for i,p in enumerate(packs):
    if p is p1 or p is p2:
        pp *= (i + 1) 

print(pp)