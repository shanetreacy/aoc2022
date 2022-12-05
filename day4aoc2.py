with open('day4.txt') as day1:
  lines = day1.readlines()

current = 0

for line in lines:
  line = line.strip()
  (range1, range2) = line.split(',')
  (start1, end1) = range1.split('-')
  (start2, end2) = range2.split('-')
 
  if (int(start1) >= int(start2) and int(end1) <= int(end2)) or (int(start2) >= int(start1) and int(end2) <= int(end1)):
    current = current + 1 
  elif int(start1) >= int(start2) and int(start1)<=int(end2):
    current = current + 1
  elif int(start2) >= int(start1) and int(start2)<=int(end1):
    current = current + 1
  elif int(end1) >= int(start2) and int(end1)<=int(end2):
    current = current + 1
  elif int(end2) >= int(start1) and int(end2)<=int(end1):
    current = current + 1


print(current)
