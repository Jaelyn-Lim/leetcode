# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 23:02
# @Author  : jaelyn
# @FileName: 136.py
# @Software: PyCharm

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans
        # ans = set()
        # for num in nums:
        #     if num in ans:
        #         ans.remove(num)
        #     else:
        #         ans.add(num)
        # return ans.pop()


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 2, 1]
    print(solution.singleNumber(nums))