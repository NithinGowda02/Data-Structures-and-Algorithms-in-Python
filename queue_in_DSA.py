class queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, element):
        self.queue.append(element) 

    def dequeue(self):
        if len(self.queue) ==  0:
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) ==  0:
            return "Queue is empty"
        return self.queue[0] 

    def length(self):
        return len(self.queue)  
    
myqueue = queue()
myqueue.enqueue("A")
myqueue.enqueue("B")    
myqueue.enqueue("C")

print(f"Enqueue >> {myqueue.queue}")
print(f"Dequeue >> {myqueue.dequeue()}")
print(f"Peek Element >> {myqueue.peek()}")
print(f"Length of Queue >> {myqueue.length()}")