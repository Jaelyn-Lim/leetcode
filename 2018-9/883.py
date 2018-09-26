# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 22:54
# @Author  : jaelyn
# @FileName: 883.py
# @Software: PyCharm

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top = 0
        front = 0
        right = 0
        for row in grid:
            right += max(row)
            for num in row:
                if num != 0:
                    top += 1
        for line in zip(*grid):
            front += max(line)
        return right + front + top


if __name__ == '__main__':
    solution = Solution()
    grid = [[1,2],[3,4]]
    print(solution.projectionArea(grid))
