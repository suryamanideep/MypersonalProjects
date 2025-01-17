#This is the only file you need to work on. You do NOT need to modify other files

# Below are the functions you need to implement. For the first project, you only need to finish implementing iddfs() 
# ie iterative deepening depth first search

# here you need to implement the Iterative Deepening Search Method
import sys
from heapq import heappop, heappush

def iterativeDeepening(puzzle):
    for depth_limit in range(sys.maxsize):
        visited = set()
        path = []
        
        result = depthLimitedDFS(puzzle, depth_limit, visited, path)
        
        if result:
            return result
        
    return []

def depthLimitedDFS(puzzle, depth_limit, visited, path):
    if puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return path
    
    if depth_limit == 0:
        return None
    
    visited.add(tuple(puzzle))
    empty_index = puzzle.index(8)
    neighbors = getNeighbors(empty_index)
    
    for neighbor in neighbors:
        new_puzzle = puzzle[:]
        new_puzzle[empty_index], new_puzzle[neighbor] = new_puzzle[neighbor], new_puzzle[empty_index]
        
        if tuple(new_puzzle) not in visited:
            result = depthLimitedDFS(new_puzzle, depth_limit - 1, visited, path + [neighbor])
            if result is not None:
                return result
    
    return None

def getNeighbors(index):
    neighbors = []
    
    if index % 3 > 0:
        neighbors.append(index - 1)
    if index % 3 < 2:
        neighbors.append(index + 1)
    if index // 3 > 0:
        neighbors.append(index - 3)
    if index // 3 < 2:
        neighbors.append(index + 3)
    
    return neighbors

def astar(puzzle):
    open_list = [(heuristic(puzzle), puzzle, [])]
    visited = set()
    while open_list:
        _, current, path = heappop(open_list)
        visited.add(tuple(current))
        
        if current == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            return path
        
        empty_index = current.index(8)
        neighbors = getNeighbors(empty_index)
        
        for neighbor in neighbors:
            new_puzzle = current[:]
            new_puzzle[empty_index], new_puzzle[neighbor] = new_puzzle[neighbor], new_puzzle[empty_index]
            if tuple(new_puzzle) not in visited:
                new_path = path + [neighbor]
                cost = len(new_path) + heuristic(new_puzzle)
                heappush(open_list, (cost, new_puzzle, new_path))
    
    return []

def heuristic(puzzle):
    distance = 0
    for i in range(9):
        row_diff = abs(i // 3 - puzzle.index(i) // 3)
        col_diff = abs(i % 3 - puzzle.index(i) % 3)
        distance += row_diff + col_diff
    return distance