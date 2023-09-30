'''
def tight_print(m):
    [print(''.join(map(str,r))) for r in m]
'''

map0 = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0],
        [0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
map1 = [[0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]]

map2a = [[1, 1, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 0], [1, 1, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1],
         [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1]]


def total_perimeter(mp):
    if not mp:
        return 0
    rows, cols = len(mp), len(mp[0])

    # Helper function to get the perimeter contribution of a single cell
    def perimeter_of_cell(i, j):
        if mp[i][j] == 0:
            return 0

        perimeter = 0
        # Check top
        if i == 0 or mp[i - 1][j] == 0:
            perimeter += 1
        # Check bottom
        if i == rows - 1 or mp[i + 1][j] == 0:
            perimeter += 1
        # Check left
        if j == 0 or mp[i][j - 1] == 0:
            perimeter += 1
        # Check right
        if j == cols - 1 or mp[i][j + 1] == 0:
            perimeter += 1

        return perimeter

    total = 0
    for i in range(rows):
        for j in range(cols):
            total += perimeter_of_cell(i, j)

    return total


#print(total_perimeter(map0))
#print(total_perimeter(map1))
#print(total_perimeter(map2a))


def max_island_perimeter(mp):
    if not mp:
        return 0

    rows, cols = len(mp), len(mp[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Helper function to check if the cell is within the grid and is land
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and mp[x][y] == 1

    # DFS function to explore each land square and calculate its contribution to the perimeter
    def dfs(x, y):
        if visited[x][y]:
            return 0
        visited[x][y] = True

        # Default perimeter for each land square
        perimeter = 4

        # Directions for horizontal and vertical neighbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                # If the neighbor is land, reduce the perimeter by 1 and continue the DFS
                perimeter -= 1
                perimeter += dfs(nx, ny)

        return perimeter

    # Iterate over each cell in the grid and if it's land and not visited, start DFS
    max_perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if mp[i][j] == 1 and not visited[i][j]:
                max_perimeter = max(max_perimeter, dfs(i, j))

    return max_perimeter

#print(max_island_perimeter(map0))
#print(max_island_perimeter(map1))
#print(max_island_perimeter(map2a))
