scoreMatrix1 = { 'A': {'X': 1+3, 'Y': 2+6, 'Z': 3+0}, 'B': {'X': 1+0, 'Y': 2+3, 'Z': 3+6}, 'C':{'X': 3+0, 'Y': 3+6, 'Z': 3+3} }
scoreMatrix2 = { 'A': {'X': 3+0, 'Y': 1+3, 'Z': 2+6}, 'B': {'X': 1+0, 'Y': 2+3, 'Z': 3+6}, 'C':{'X': 2+0, 'Y': 3+3, 'Z': 1+6} }

with open('day2.txt') as data:
  lines = data.readlines()

points1 = 0
points2 = 0

for line in lines:
  (them, me) = line.strip().split()
  points1 = points1 + scoreMatrix1[them][me]
  points2 = points2 + scoreMatrix2[them][me]

print(f"Points 1 {points1}")
print(f"Points 2 {points2}")
