from collections import deque

with open('day6.txt') as day6:
  lines = day6.readlines()

target_size = 14
current = 0

buffer = deque([''] * target_size)

for line in lines:
  for char in line:
    current = current + 1
    buffer.popleft()
    buffer.append(char)
    if current > target_size and len(set(buffer)) == target_size:
      print(current)
      break
