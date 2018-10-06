# -*- coding: utf-8 -*-
# @Time    : 2018/10/6 15:31
# @Author  : jaelyn
# @FileName: 766.py
# @Software: PyCharm

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return False
        for i in range(len(matrix) - 1):
            print(matrix[i][:-1])
            print(matrix[i + 1][1:])
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True

        # ans = [-1 for i in range(len(matrix)+len(matrix[0])-1)]
        # for index, nums in enumerate(matrix[::-1]):
        #     temp = index
        #     for num in nums:
        #         if ans[temp] == -1:
        #             ans[temp] = num
        #         elif ans[temp] != num:
        #             return False
        #         temp += 1
        # return True

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    # matrix = [[1, 2], [2, 2]]
    print(solution.isToeplitzMatrix(matrix))