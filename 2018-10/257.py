# -*- coding: utf-8 -*-
# @Time    : 2018/10/6 17:16
# @Author  : jaelyn
# @FileName: 257.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        stack = [(root, '')]
        while stack:
            node, p = stack.pop()
            if node:
                if not (node.left or node.right):
                    result.append(p + str(node.val))
                stack += [(node.right, p + str(node.val) + '->'), (node.left, p + str(node.val) + '->')]
        return result


if __name__ == '__main__':
    solution = Solution()

    t1 = TreeNode(1)
    t1.right = TreeNode(3)
    t2 = TreeNode(2)
    t2.right = TreeNode(5)
    t1.left = t2

    print(solution.binaryTreePaths(t1))

