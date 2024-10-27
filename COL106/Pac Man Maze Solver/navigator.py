from maze import *
from exception import *
from stack import *


class PacMan:
    def __init__(self, grid: Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def copy_route(self,route) -> list:
        copy_route=[]
        for item in route:
           copy_route.append(item)
        return copy_route 
    def solve(self, start, end, grid, ans, m, n) -> bool:
        if self.navigator_maze[start[0]][start[1]] == 1:
            return False
        if self.navigator_maze[end[0]][end[1]] == 1:
            return False
        
        (x, y) = start
        route = [(x, y)]
        stack = Stack()
        stack.push(((x, y), route))
        
        while stack.get_size() > 0:
            currcell, route = stack.pop()
            (x, y) = currcell
            
            grid[x][y] = True 
            if self.navigator_maze[x][y]==1:
                  continue
            if (x, y) == end:
                ans.extend(route)
                return True
            
            # Move down
            if x + 1 < m and not grid[x + 1][y]:
                newroute = self.copy_route(route)
                newroute.append((x + 1, y))
                stack.push(((x + 1, y), newroute))

            # Move right
            if y + 1 < n and not grid[x][y + 1]:
                newroute = self.copy_route(route)
                newroute.append((x, y + 1))
                stack.push(((x, y + 1), newroute))   

            # Move up
            if x - 1 >= 0 and not grid[x - 1][y]:
                newroute = self.copy_route(route)
                newroute.append((x - 1, y))
                stack.push(((x - 1, y), newroute))

            # Move left
            if y - 1 >= 0 and not grid[x][y - 1]:
                newroute = self.copy_route(route)
                newroute.append((x, y - 1))
                stack.push(((x, y - 1), newroute))

        return False

    def find_path(self, start, end) -> list:
        m = len(self.navigator_maze)
        n = len(self.navigator_maze[0])
        self.grid = [[False for _ in range(n)] for _ in range(m)]
        
        ans = []
        if self.solve(start, end, self.grid, ans, m, n):
            return ans
        else:   
            raise PathNotFoundException
