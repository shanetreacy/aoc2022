with open('day1.txt') as day1:
  lines = day1.readlines()

current = 0

for line in lines:
  line = line.strip()

  if line != "":
    current = current + int(line)
  else :
    print(current)  
    current = 0


print(current)

# 1 : python3 day1aoc.py | sort -n | tail -1 
# 2 : python3 day1aoc.py | sort -n | tail -3 | paste -sd+ - | bc 
