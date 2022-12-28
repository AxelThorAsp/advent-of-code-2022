from heapq import heappush, heappop
import itertools

class myHeap:
    def __init__(self) -> None: 
        self.pq = []                        
        self.entry_finder = {}              
        self.REMOVED = '<removed-task>'     
        self.counter = itertools.count()    
    
    def add_task(self, task, priority=0) -> None:
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)
    
    def remove_task(self,task) -> None:
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED
    
    def pop_task(self) -> object:
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

    def is_empty(self) -> bool:
        return len(self.entry_finder) == 0

    def __repr__(self) -> str:
        return str(self.pq)

def test():
    pq = myHeap()
    pq.add_task('A', 1)
    pq.add_task('B', 2)
    pq.add_task('A', 3)
    print(pq.entry_finder)
    print(pq.pq)
    print(pq.is_empty())

test()