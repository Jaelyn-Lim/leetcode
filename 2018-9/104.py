# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午4:24
# @Author  : jaelyn
# @FileName: 104.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root == None:
        #     return 0
        # m1 = self.maxDepth(root.left) + 1
        # m2 = self.maxDepth(root.right) + 1
        return 0 if root is None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



if __name__ == '__main__':
    solution = Solution()
    t_20 = TreeNode(20)
    t_20.left = TreeNode(15)
    t_20.right = TreeNode(7)

    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = t_20

    result = solution.maxDepth(t)
    print(result)
