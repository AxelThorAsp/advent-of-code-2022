from functools import total_ordering
@total_ordering
class Node():
    def __init__(self, _id, dist, src = None):
        self._id = _id 
        self.dist = dist 
        self.src = src
        self.nbors = [] 
    
    def __lt__(self, obj: object):
        return ((self.dist) < (obj.dist))
    
    def __gt__(self, obj):
        return ((self.dist) > (obj.dist))
    
    def __le__(self, obj):
        return ((self.dist) <= (obj.dist))
    
    def __ge__(self, obj):
        return ((self.dist) >= (obj.dist)) 
    
    def __eq__(self, obj):
        return ((self.dist) == (obj.dist))
    
    def __hash__(self):
        return int(self._id) 
    
    def __repr__(self):
        return "(" + str(self._id) + ", " + str(self.dist)+ ")"