import sys 
filepath = sys.argv[1]
lines = [l.split('\n') for l in open(filepath).read().split('\n\n')]

def car(l):
    return l[0]

def cdr(l):
    if not len(l):
        raise KeyError("empty list in cdr")
    return l[1:]

def li(i):
    return [i]

def compare(l, r):
    ll = car(l)
    rr = car(r)
    print(ll,rr)
    if type(ll) == int and type(rr) == int:
        if ll < rr:
            return True
        else:
            return None
    elif type(ll) == list and type(rr) == list:
        if len(ll) == 0 and len(rr) != 0:
            return True 
        if len(rr) == 0 and len(ll) != 0:
            return False
        ret = compare(ll,rr)
        if ret:
            return True
    elif type(ll) == int:
        if len(rr) == 0:
            return False
        ret = compare([ll],rr)
        if ret:
            return True 
    elif type(rr) == int:
        if len(ll) == 0:
            return True
        ret = compare(ll,[rr])
        if ret:
            return True 
    return compare(cdr(l),cdr(r))

c = 0
i = 0
for ll in lines:
    i += 1
    l = eval(ll[0])
    r = eval(ll[1])
    print(compare(l,r))