queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Peek
frontElement = queue[0]
print("Peek: ", frontElement)

# Dequeue
dequeuedElement = queue.pop(0)
print("Dequeue: ", dequeuedElement)

print("Queue after Dequeue: ", queue)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))