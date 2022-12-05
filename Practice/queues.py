import time
import threading
from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

food_order=Queue()
def place_order(orders):
    for order in orders:
        time.sleep(0.5)
        food_order.enqueue(order)

def serve_order(orders):
    time.sleep(1)
    while True:
        order=food_order.dequeue()
        time.sleep(2)


if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()

#Write a program to print binary numbers from 1 to 10 using Queue. 
# Use Queue class implemented in main tutorial. Binary sequence should look like,
