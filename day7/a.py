import sys

filepath = sys.argv[1]

class File:
    def __init__(self, name, size, dir):
        self.name = name
        self.size = size
        self.dir = dir

class Directory:

    files = []
    parent = None

    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
    
    def __repr__(self):
        return self.name

    def get_parent(self):
        return self.parent



l = map(lambda x: x.strip(),open(filepath).readlines())

line = ''
for cmd in l:
    if cmd.startswith('$'):
        op = cmd.split()
        if op[1] == 'ls':
            pass
        else:
            cd = op[2]
            if cd == '/':
                wd = Directory('/')
                print(wd)
            elif cd != '..':
                line += '-'
                wd = Directory(cd, wd)
                print(line, end='')
                print(wd)
            else:
                line = line[:-1]
                wd = wd.get_parent()
                print(line, end='')
                print(wd)
    
    elif cmd.startswith('dir'):
            pass
    else:
        pass