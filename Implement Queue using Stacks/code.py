class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return f'{self.data}'


class Stack:
    def __init__(self):
        self.head = None
        
    
    def push(self, item):
        self.head = Node(item, self.head)

    
    def pop(self):
        item = self.head.data
        self.head = self.head.next
        return item
    
    def peek(self):
        return self.head.data
    
    def empty(self):
        return self.head is None


class MyQueue:

    def __init__(self):
        self.stack_main = Stack()
        self.stack_help = Stack()
        

    def push(self, x: int) -> None:
                
        while not self.stack_main.empty():
            self.stack_help.push(self.stack_main.pop())
        
        self.stack_main.push(x)
        
        while not self.stack_help.empty():
            self.stack_main.push(self.stack_help.pop())


    
        # if self.stack_main.head is None:
        #     self.stack_main.push(x)
        # else:
        #     probe = self.stack_main.head
        #     while probe is not None:
        #         self.stack_help.push(probe)
        #         self.stack_main.pop()
        #         probe = probe.next

        #     self.stack_main.push(x)
            
        #     probe = self.stack_help.head
        #     while probe is not None:
        #         self.stack_main.push(probe)
        #         self.stack_help.pop()
        #         probe = probe.next
            

    def pop(self) -> int:
        # return self.stack_main.pop()
        item = self.stack_main.peek()
        self.stack_main.pop()
        return item
    

    def peek(self) -> int:
        return self.stack_main.peek()
        

    def empty(self) -> bool:
        return self.stack_main.empty()

    def __str__(self):
        s = ''
        current = self.stack_main.head
        while current is not None:
            s += str(current.data)+' '
            current = current.next
        return f'start -> {s}<- end'
      


# Your MyQueue object will be instantiated and called as such:
# x=1
# obj = MyQueue()
# obj.push(x)
# obj.push(2)
# print(obj)
# param_3 = obj.peek()
# print(param_3)
# param_2 = obj.pop()
# print(obj)
# param_4 = obj.empty()
# print(obj)