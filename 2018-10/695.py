# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 23:23
# @Author  : jaelyn
# @FileName: 695.py
# @Software: PyCharm

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for index_x, line in enumerate(grid):
            for index_y, num in enumerate(line):
                if num > 0:
                    temp = num
                    flag = 0
                    if index_y-1 >= 0 and grid[index_x][index_y-1] > 0:
                        temp += grid[index_x][index_y-1]
                        flag += 1
                    if index_x-1 >= 0 and grid[index_x-1][index_y] > 0:
                        temp += grid[index_x-1][index_y]
                        flag += 1
                    if flag == 2:
                        temp -= 1
                    if temp > ans:
                        ans = temp
                    grid[index_x][index_y] = temp
        # for x in grid:
        #     for y in x:
        #         print(y, end=' ')
        #     print()
        return ans



if __name__ == '__main__':
    solution = Solution()
    # grid = [
    #     [0,0,1,0,0,0,0,1,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #     [0,1,1,0,1,0,0,0,0,0,0,0,0],
    #     [0,1,0,0,1,1,0,0,1,0,1,0,0],
    #     [0,1,0,0,1,1,0,0,1,1,1,0,0],
    #     [0,0,0,0,0,0,0,0,0,0,1,0,0],
    #     [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #     [0,0,0,0,0,0,0,1,1,0,0,0,0]
    #          ]

    grid = [
        [1,1,0,1,1],
        [1,0,0,0,0],
        [0,0,0,0,1],
        [1,1,0,1,1]
    ]
    print(solution.maxAreaOfIsland(grid))
