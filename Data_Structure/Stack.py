class Stack():
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)             

    def remove(self):
        return self.items.pop()
    
    def is_empty(self):
        if self.items == []:
            return 'No one in the queue'
        else:
            return 'Busy'
    
    def last(self):
        if not self.is_empty():
            return self.items[-1]
