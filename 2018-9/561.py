# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 下午10:46
# @Author  : jaelyn
# @FileName: 561.py
# @Software: PyCharm

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    solution = Solution()
    nums = [7,3,1,0,0,6]
    ret = solution.arrayPairSum(nums)
    print(ret)