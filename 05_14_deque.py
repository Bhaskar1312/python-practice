from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.appendleft(-2)
print(queue)
queue.popleft()
queue.popleft()
queue.pop()
# queue.pop()
if not queue:
    print("empty")
print(queue)