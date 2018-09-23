# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 上午12:11
# @Author  : jaelyn
# @FileName: 118.py
# @Software: PyCharm

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for row in range(numRows):
            row_list = []
            for num in range(row+1):
                if row >= 0 and row != num and num > 0:
                    row_list.append(ans[row-1][num]+ans[row-1][num-1])
                else:
                    row_list.append(1)
            ans.append(row_list)
        return ans


if __name__ == '__main__':
    solution = Solution()
    numRows = 5
    print(solution.generate(numRows))
