# -*- coding: utf-8 -*-
# @Time    : 2018/10/6 18:28
# @Author  : jaelyn
# @FileName: 700.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # if root:
        #     if root.val == val:
        #         return root
        #     return self.searchBST(root.left, val) or self.searchBST(root.right, val)
        if not root:
            return root
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right

if __name__ == '__main__':
    solution = Solution()

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t4 = TreeNode(4)
    t4.left = t2
    t4.right = TreeNode(7)

    val = 2

    print(solution.searchBST(t4, val))
