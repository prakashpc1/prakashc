class stack:
    def __init__(self):
       self.items=[]
    def isEmpty(self):
       return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def display(self):
        return (self.items)
s=stack()
print(s.isEmpty())
print("push operations")
s.push(11)
s.push(12)
s.push(13)
print("size:",s.size())
print(s.display())
print("pop operations")
print(s.pop())
print(s.pop())
print(s.display())
print("size:",s.size())