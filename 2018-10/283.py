# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 23:19
# @Author  : jaelyn
# @FileName: 283.py
# @Software: PyCharm

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for index, num in enumerate(nums):
            if num == 0:
                for i, n in enumerate(nums[index:]):
                    if n != 0:
                        nums[i+index], nums[index] = nums[index], n
                        break
        return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,0,3,12]
    print(solution.moveZeroes(nums))

