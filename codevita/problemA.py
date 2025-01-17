from collections import deque

# Rotations for the move rule (right, left, backward rotations)
def rotate_right(x, y):
    return y, -x

def rotate_left(x, y):
    return -y, x

def rotate_back(x, y):
    return -x, -y

# BFS algorithm to find the minimum number of moves
def min_moves_to_destination(grid, M, N, source, dest, move_rule):
    # Initialize BFS
    queue = deque([(source[0], source[1], 0)])  # (row, col, distance)
    visited = set()
    visited.add((source[0], source[1]))
    
    move_directions = [
        lambda x, y: (x + move_rule[0], y + move_rule[1]),  # forward
        lambda x, y: (x + rotate_right(*move_rule)[0], y + rotate_right(*move_rule)[1]),  # right
        lambda x, y: (x + rotate_left(*move_rule)[0], y + rotate_left(*move_rule)[1]),  # left
        lambda x, y: (x + rotate_back(*move_rule)[0], y + rotate_back(*move_rule)[1]),  # back
    ]
    
    # BFS Loop
    while queue:
        x, y, dist = queue.popleft()
        
        # If destination is reached
        if (x, y) == dest:
            return dist
        
        # Explore all directions
        for move in move_directions:
            new_x, new_y = move(x, y)
            
            # Check if the move is valid (inside the grid and the cell is 0)
            if 0 <= new_x < M and 0 <= new_y < N and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, dist + 1))
    
    # If destination is unreachable
    return -1

# Input Reading
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
source = tuple(map(int, input().split()))
dest = tuple(map(int, input().split()))
move_rule = tuple(map(int, input().split()))

# Output the result
result = min_moves_to_destination(grid, M, N, source, dest, move_rule)
print(result)