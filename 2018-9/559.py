# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 下午6:14
# @Author  : jaelyn
# @FileName: 559.py
# @Software: PyCharm

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        max_deep = 1
        if root.children:
            for child in root.children:
                child_max_deep = self.maxDepth(child) + 1
                if child_max_deep > max_deep:
                    max_deep = child_max_deep
        return max_deep

if __name__ == '__main__':
    solution = Solution()
    node5 = Node(5, None)
    node6 = Node(6, None)
    node3 = Node(3, [node5, node6])
    node2 = Node(2, None)
    node4 = Node(4, None)

    root = Node(1, [node3, node2, node4])
    ret = solution.maxDepth(root)
    print(ret)