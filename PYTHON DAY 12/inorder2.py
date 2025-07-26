from collections import deque
queue = deque([1,2,3])
queue.append(queue.popleft())
queue.popleft()
print(["hai" for i in queue])

