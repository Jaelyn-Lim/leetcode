# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 下午11:43
# @Author  : jaelyn
# @FileName: 108.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


if __name__ == '__main__':
    solution = Solution()
    nums = [-10,-3,0,5,9]
    ret = solution.sortedArrayToBST(nums)
    print(ret)