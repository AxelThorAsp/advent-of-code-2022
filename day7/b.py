import sys

DISC = 70000000

REQ = 30000000

filepath = sys.argv[1]
class Directory:

    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.files = []
        self.subdirs = {}
    
    def __repr__(self):
        return self.name

    def get_parent(self):
        return self.parent
    
    def add_file(self, size):
        self.files.append(size)

    
dirs = {}


l = map(lambda x: x.strip(),open(filepath).readlines())


for cmd in l:
    if cmd.startswith('$'):
        op = cmd.split()
        if op[1] == 'ls':
            pass
        else:
            cd = op[2]
            if cd == '/':
                wd = Directory('/')
                dirs['root'] = wd
            elif cd != '..':
                wd = wd.subdirs[cd]
            else:
                if wd.name != '/':
                    wd = wd.get_parent()
    
    elif cmd.startswith('dir'):
        _dir = cmd.split()[1]
        dir_object = Directory(_dir, wd)
        wd.subdirs[_dir] = dir_object
        dirs[_dir + str(id(wd))] = dir_object 
    else:
        wd.add_file(int(cmd.split()[0]))


def sum_(dr):
    s = sum(dr.files)
    for subdr in dr.subdirs:
        s += sum_(dr.subdirs[subdr])
    return s


UNUSED = DISC -  sum_(dirs['root'])
MIN = REQ - UNUSED


def min_max():
    smol = float('inf')
    for v in dirs.values():
        _ = sum_(v)
        if _ <= smol and _ >= MIN:
            smol = _           
    return smol

print(min_max())