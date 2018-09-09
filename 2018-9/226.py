# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 上午12:44
# @Author  : jaelyn
# @FileName: 226.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        # temp_tree = root.left
        # root.left = self.invertTree(root.right)
        # root.right = self.invertTree(temp_tree)
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == '__main__':
    t_l = TreeNode(2)
    t_l.left = TreeNode(1)
    t_l.right = TreeNode(3)

    t_r = TreeNode(7)
    t_r.left = TreeNode(6)
    t_r.right = TreeNode(9)

    t = TreeNode(4)
    t.left = t_l
    t.right = t_r

    solution = Solution()
    result = solution.invertTree(t)
    print(result)