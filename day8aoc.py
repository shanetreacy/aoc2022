def make_grid(lines):
  grid = []

  for line in lines:
    row = []
    for c in line.strip():
      row.append(int(c))
    grid.append(row)

  return grid

def make_visiblility_map(grid):
  row_length = len(grid[0])
  col_length = len(grid)

  return [ [False] * row_length for i in range(col_length)] 

def calculate_visibility_from_left(grid, map):
  for row_index, row in enumerate(grid):
    max_height=-1
    for col_index, tree in enumerate(row):
      if tree > max_height:
        max_height = tree
        map[row_index][col_index] = True

def calculate_visibility_from_right(grid, map):
  for row_index, row in enumerate(grid):
    max_height=-1
    for col_index in reversed(range(len(row))):
      tree = row[col_index]
      if tree > max_height:
        max_height = tree
        map[row_index][col_index] = True

def calculate_visibility_from_top(grid, map):
  for col_index in range(len(grid[0])):
    max_height=-1
    for row_index in range(len(grid)):
      tree = grid[row_index][col_index]
      if tree > max_height:
        max_height = tree
        map[row_index][col_index] = True

def calculate_visibility_from_bottom(grid, map):
  for col_index in range(len(grid[0])):
    max_height=-1
    for row_index in reversed(range(len(grid))):
      tree = grid[row_index][col_index]
      if tree > max_height:
        max_height = tree
        map[row_index][col_index] = True


def calculate_visibility(grid):
  map = make_visiblility_map(grid)

  calculate_visibility_from_left(grid, map)
  calculate_visibility_from_right(grid, map)
  calculate_visibility_from_top(grid, map)
  calculate_visibility_from_bottom(grid, map)

  total = 0

  for row in map:
    for tree in row:
      if tree:
        total = total + 1
  
  return total

def up(grid, row, col):
  tree = grid[row][col]
  score = 0

  for t in reversed(range(row)):
    score = score + 1
    if grid[t][col] >= tree:
      break

  return score

def down(grid, row, col):
  tree = grid[row][col]
  score = 0

  for t in range(row+1, len(grid)):
    score = score + 1
    if grid[t][col] >= tree:
      break

  return score

def left(grid, row, col):
  tree = grid[row][col]
  score = 0

  for t in reversed(range(col)):
    score = score + 1
    if grid[row][t] >= tree:
      break
  
  return score

def right(grid, row, col):
  tree = grid[row][col]
  score = 0

  for t in range(col+1, len(grid[row])):
    score = score + 1
    if grid[row][t] >= tree:
      break
  
  return score

def calculate_scenic_score(grid, row, col):
  tree = grid[row][col]

  return up(grid, row,col) * down(grid, row, col) * left(grid, row, col) * right(grid, row, col) 
  
def calculate_best_scenic_score(grid):
  best = 0
  for row_index, row in enumerate(grid):
    for col_index, _ in enumerate(row):
      score = calculate_scenic_score(grid, row_index, col_index)
      if score > best:
        best = score

  return best

def test_the_thing():
  test_lines = '''30373
25512
65332
33549
35390'''.split('\n')

  grid = make_grid(test_lines)
  total = calculate_visibility(grid)
  
  assert total == 21

  best_secenic_core = calculate_best_scenic_score(grid)

  assert best_secenic_core == 8

with open('day8.txt') as day8:
  lines = day8.readlines()
  grid = make_grid(lines)
  print(f"Visibility = {calculate_visibility(grid)}")
  print(f"Best scenic score = {calculate_best_scenic_score(grid)}")
