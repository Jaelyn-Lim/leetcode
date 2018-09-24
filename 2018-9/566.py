# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 22:55
# @Author  : jaelyn
# @FileName: 566.py
# @Software: PyCharm

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(nums)*len(nums[0]):
            return nums
        ans = []
        new_row = []
        for row_line in nums:
            for num in row_line:
                new_row.append(num)
                if len(new_row) == c:
                    ans.append(new_row)
                    new_row = []
        return ans



if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(solution.matrixReshape(nums, r, c))