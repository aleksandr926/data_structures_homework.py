# class Node:
#    def __init__(self):
#       self.node = []
#
#    def update(self, key):
#       i_f = False
#       for i, k in enumerate(self.node):
#          if key == k:
#             self.node[i] = key
#             i_f = True
#             break
#       if not i_f:
#          self.node.append(key)
#
#    def get(self, key):
#       for k in self.node:
#          if k == key:
#             return True
#       return False
#
#    def remove(self, key):
#       for i, k in enumerate(self.node):
#          if key == k:
#             del self.node[i]
# class HashSet:
#    def __init__(self):
#       self.space_key = 1234
#       self.hash_map = [Node() for i in range(self.space_key)]
#
#    def cont(self, key):
#       hash_key = key % self.space_key
#       return self.hash_map[hash_key].get(key)
#
#    def add(self, key):
#       hash_key = key % self.space_key
#       self.hash_map[hash_key].update(key)
#
#    def remove(self, key):
#       hash_key = key % self.space_key
#       self.hash_map[hash_key].remove(key)
#
# y = Node()
# print(y.update())
# print(y.get())
# x = HashSet()
# print(x.cont())
# print(x.add())
# print(x.remove())