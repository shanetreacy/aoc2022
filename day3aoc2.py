from itertools import islice

def half(text):
  return (text[:len(text)//2], text[len(text)//2:])

def find_common(text1, text2, text3):
  return list(set(text1) & set(text2) & set(text3))[0]

def priority(item):
  ascii = ord(item)
  if ascii >= 97:
    return ascii - 96
  else:
    return ascii - 64 + 26 

total_priority = 0

with open('day3.txt') as data:
  while True:
    lines = list(islice(data, 3))
    if not lines:
      break

    
    item = find_common(lines[0].strip(), lines[1].strip(), lines[2].strip()) 
    total_priority = total_priority + priority(item)

print(f"{total_priority}")
