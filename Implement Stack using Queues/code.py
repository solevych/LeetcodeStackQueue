class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return f'{self.item}'

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    def peek(self):
        if self.head:
            return self.head.item
        return -1

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return len(self) == 0

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.item)+' '
            current = current.next
        return f'start -> {s}<- end'


class MyStack:

    def __init__(self):
        self.queue_main = Queue()
        self.queue_help = Queue()
        

    def push(self, x: int) -> None:
        self.queue_main.push(x)
   

    def pop(self) -> int:
        if self.queue_main.head.next is None:
            item = self.queue_main.head.item
            self.queue_main.head = None
            return int(item)
        
        while self.queue_main.head.next is not None:
            self.queue_help.push(self.queue_main.pop().item)

        # print(self.queue_help)
        # print(self.queue_main)
        item = self.queue_main.pop().item
     

        while not self.queue_help.is_empty():
            self.queue_main.push(self.queue_help.pop().item)

        return item

    def top(self) -> int:
        if self.queue_main is not None:
            return int(self.queue_main.tail.item)
        

    def empty(self) -> bool:
        return self.queue_main.is_empty()

    def __str__(self):
        return str(self.queue_main)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# print(obj)
# param_2 = obj.pop()
# # print(obj)
# print(obj.top())
# print(obj.empty())