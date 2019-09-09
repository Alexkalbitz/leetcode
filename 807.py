# In a 2 dimensional array grid, each value grid[i][j] represents the height 
# of a building located there. We are allowed to increase the height of any 
# number of buildings, by any amount 
# (the amounts can be different for different buildings). 
# Height 0 is considered to be a building as well.
#
# At the end, the "skyline" when viewed from all four directions of 
# the grid, i.e. top, bottom, left, and right, must be the same as the 
# skyline of the original grid. A city's skyline is the outer contour 
# of the rectangles formed by all the buildings when viewed from a distance. 
# See the following example.
#
# What is the maximum total sum that the height of the buildings can be increased?
#
# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation:
# The grid is:
# [ [3, 0, 8, 4],
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]
#
# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]
#
# The grid after increasing the height of buildings without affecting skylines is:
#
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_from_side = self.side_view(grid)
        max_from_top = self.top_view(grid)
        max_increase = 0
        for row in range(0, len(grid)):
            for house in range(0, len(grid[0])):
                if max_from_side[row] < max_from_top[house]:
                    cur_max = max_from_side[row]
                else:
                    cur_max = max_from_top[house]
                if (cur_max) > grid[row][house]:
                    max_increase += (cur_max) - grid[row][house]
        return max_increase

    def side_view(self, grid):
        biggest = 0
        skyline = []
        for row in grid:
            for building in row:
                if building > biggest:
                    biggest = building
            skyline.append(biggest)
            biggest = 0
        return skyline

    def top_view(self, grid):
        biggest = 0
        skyline = []
        for column in range(0, len(grid[0])):
            for building in range(0, len(grid)):
                if grid[building][column] > biggest:
                    biggest = grid[building][column]
            skyline.append(biggest)
            biggest = 0
        return skyline


test = [[3, 0, 8, 4],
        [2, 4, 5, 7],
        [9, 2, 6, 3],
        [0, 3, 1, 0]]

test2 = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 2, 6, 3],
         [1, 1, 1, 1]]

test3 = [[9, 9],
         [9, 1],
         [9, 1],
         [9, 1]]

s = Solution()
result = s.maxIncreaseKeepingSkyline(test)
print(result)

