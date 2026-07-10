class Stack:
    def __init__(self):
        self.stack = []

    
    def push(self):
        self.stack.append(item)
        

    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("empty stack")

    
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek form empty stack ")



class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self , item):
        self.queue.append(items)
        print(f"{item}added to the queue")

     def dequeue(self):
        if self.is_empty():
            print("queue is empty") 
            return None
       return self.queue.pop(0)
    
    def front(self):
        if self.is_empty():
            print("no front element")
            return None
        return self.queue(0)



