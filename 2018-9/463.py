# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 23:12
# @Author  : jaelyn
# @FileName: 463.py
# @Software: PyCharm


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for row_index, row in enumerate(grid):
            for index, num in enumerate(row):
                if num == 1:
                    temp = 4
                    if row_index != 0:
                        if grid[row_index-1][index] == 1:
                            temp -= 1
                    if index != 0:
                        if grid[row_index][index-1] == 1:
                            temp -= 1
                    if row_index + 1 != len(grid):
                        if grid[row_index+1][index] == 1:
                            temp -= 1
                    if index + 1 != len(grid[0]):
                        if grid[row_index][index+1] == 1:
                            temp -= 1
                    ans += temp
        return ans


if __name__ == '__main__':
    solution = Solution()
    grid =   [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    print(solution.islandPerimeter(grid))