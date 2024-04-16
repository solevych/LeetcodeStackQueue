class Node:
    def __init__(self, data, next= None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return f"Node({self.data})"

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
    
    def __str__(self):
        s = ''
        cur = self.head
        while cur is not None:
            s = str(cur.data) + ' ' +s
            cur = cur.next
        return 'bottom -> '+ s + '<- top'

class FreqStack:

    def __init__(self):
        self.stack = Stack()
        self.values = {}
        self.max_count = 0

    def push(self, val: int) -> None:
        self.stack.push(val)
        if val not in self.values.keys():
            self.values[self.stack.head.data] = 1
        else:
            self.values[self.stack.head.data] +=1

        if self.values[val] > self.max_count:
            self.max_count = self.values[val]

    def pop(self) -> int:

        probe = self.stack.head
        prev = None

        self.max_count = max(self.values.values())
        while probe is not None:
            if self.values[probe.data] == self.max_count:
                if prev:
                    prev.next = probe.next if probe.next else None
                else:
                    self.stack.head = probe.next if probe.next else None
                self.values[probe.data] -= 1
                break
            prev = probe
            probe = probe.next
        return probe.data


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()