from my_queue import Queue

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.print()

print(queue.read() == 1)
queue.dequeue()
queue.print()
