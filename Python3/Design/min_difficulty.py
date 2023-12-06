"""
Galactic Surfing Expedition

The cross-galaxy spacecraft course at the InterGalactic Surfing  is described by an M x N grid of planetary temperatures (1 <= M,N <= 500), each temperature being in the range 0 .. 1,000,000,000.
Some of the planets in this grid are designated as waypoints for the course. The Jedi Masters organizing the Galactic Surfing want to assign a difficulty rating D to the entire course so that a Jedi can reach any waypoint from any other waypoint by repeatedly flying from a planet to an adjacent planet with an absolute temperature difference at most D. Two planets are adjacent if one is directly north, south, east, or west of the other. The difficulty rating of the course is the minimum value of D such that all waypoints are mutually reachable in this fashion.

INPUT FORMAT:
*  Line 1: The integers M and N.
* * Lines 2..1+M: Each of these M lines contains N integer tempuratures.
* 
* * Lines 2+M..1+2M: Each of these M lines contains N values that are
*         either 0 or 1, with 1 indicating a cell that is a waypoint.
* 
Sample input
* 
* 3 5
* 20 21 18 99 5
* 19 22 20 16 26
* 18 17 40 60 80
* 1 0 0 0 1
* 0 0 0 0 0
* 0 0 0 0 1
* 
* INPUT DETAILS:
* 
* The planet course is described by a 3 x 5 grid of temperatures.  The upper-left,
* upper-right, and lower-right cells are designated as waypoints.
* 
* OUTPUT FORMAT:
* 
* * Line 1: The difficulty rating for the course (the minimum value of D
*         such that all waypoints are still reachable from each-other).
* 
* SAMPLE OUTPUT
* 
* 21
* 
* OUTPUT DETAILS:
* If D = 21, the three waypoints are reachable from each-other.  If D < 21,
* then the uppe
"""


def is_possible(grid, difficulty, waypoints):
    """
    Check if it's possible to reach all waypoints with the given difficulty rating.
    """
    # Create a copy of the grid to mark visited cells
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    def dfs(x, y):
        """
        Depth-first search to explore reachable cells from the current cell.
        """
        # Mark the current cell as visited
        visited[x][y] = True
        
        # Define the four possible directions (north, south, east, west)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny]:
                # Check if the absolute temperature difference is within the difficulty rating
                if abs(grid[nx][ny] - grid[x][y]) <= difficulty:
                    dfs(nx, ny)
    
    # Find the starting point (first waypoint)
    start_x, start_y = -1, -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if waypoints[i][j] == 1:
                start_x, start_y = i, j
                break
    
    # Perform DFS from the starting point
    dfs(start_x, start_y)
    
    # Check if all waypoints are reachable
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if waypoints[i][j] == 1 and not visited[i][j]:
                return False
    
    return True

def min_difficulty(grid, waypoints):
    """
    Perform binary search to find the minimum difficulty rating D.
    """
    low, high = 0, int(1e9)
    
    while low < high:
        mid = (low + high) // 2
        if is_possible(grid, mid, waypoints):
            high = mid
        else:
            low = mid + 1
    
    return low

# Sample input
M, N = 3, 5
grid = [[20, 21, 18, 99, 5], [19, 22, 20, 16, 26], [18, 17, 40, 60, 80]]
waypoints = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]

# Calculate and print the minimum difficulty rating
result = min_difficulty(grid, waypoints)
print(result)
