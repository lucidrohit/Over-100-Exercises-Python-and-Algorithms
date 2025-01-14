#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

class Node:
    def __init__(self, value=None):
        self.value = value 
        self.next = None

class StackwithNodes:
    ''' Define a Stack with nodes'''
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return bool(self.top)

    def pop(self):
        node = self.top
        self.top = node.next
        return node.value

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def size(self):
        node = self.top
        if node not None: num_nodes = 1
        else: return 0
        while node.next:
            num_nodes += 1
            node = node.next
        return num_nodes

    def peek(self):
        return self.top.value
        
        
def main():
    stack = StackwithNodes()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.size())    
    print(stack.peek())   
    print(stack.pop())  
    print(stack.peek())    

if __name__ == '__main__':
    main()
