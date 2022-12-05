def half(text):
  return (text[:len(text)//2], text[len(text)//2:])

def find_common(text1, text2):
  return list(set(text1) & set(text2))[0]

def priority(item):
  ascii = ord(item)
  if ascii >= 97:
    return ascii - 96
  else:
    return ascii - 64 + 26 

with open('day3.txt') as data:
  lines = data.readlines()

total_priority = 0

for line in lines:
  (compartment1, compartment2) = half(line.strip())
  item = find_common(compartment1, compartment2) 
  total_priority = total_priority + priority(item)

print(f"{total_priority}")
