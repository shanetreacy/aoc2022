from collections import deque

stack_strings = ['', 'RGJBTVZ', 'JRVL', 'SQF', 'ZHNLFVQG', 'RQTJCSMW', 'SWTCHF', 'DZCVFNJ', 'LGZDWRFQ', 'JBWVP']

stacks=[] 

for stack_string in stack_strings:
  stack = deque()
  for item in stack_string:
    stack.append(item)
  stacks.append(stack)

with open('day5.txt') as day5:
  lines = day5.readlines()

for line in lines:
  (_, move_num, _, from_stack, _,  to_stack) = line.strip().split()
  move_num = int(move_num)
  from_stack = int(from_stack)
  to_stack = int(to_stack)

  for moves in range(move_num):
    item = stacks[from_stack].pop()
    stacks[to_stack].append(item)

print(''.join(list(map(lambda s: s.pop(), stacks[1:10]))))
