class Deque():

  def __init__(self):
    self.deq = []


  def addFront(self,j):
    self.deq.insert(0,j)


  def addBack(self,j):
    self.deq.append(j)


  def removeFront(self):
    self.deq.pop(0)


  def removeBack(self):
    self.deq.pop()


  def isEmpty(self):
    return self.deq == []


  def size(self):
    return len(self.deq)






d = Deque()
d.addFront(2)
d.addFront(1)
print(d.size())
d.addBack(3)
print(d.size())
d.removeFront()
d.removeBack()
print(d.size())
d.removeFront()
print(d.isEmpty())
