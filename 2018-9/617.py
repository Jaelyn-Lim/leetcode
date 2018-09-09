# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午3:28
# @Author  : jaelyn
# @FileName: 617.py
# @Software: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
        # return self.build_tree(t1, t2)

    def build_tree(self, tree_01, tree_02):
        root = TreeNode(0)

        if tree_01 is None and tree_02 is None:
            root = None

        elif tree_01 is None:
            root.val = tree_02.val
            root.left = self.build_tree(None, tree_02.left)
            root.right = self.build_tree(None, tree_02.right)
        elif tree_02 is None:
            root.val = tree_01.val
            root.left = self.build_tree(tree_01.left, None)
            root.right = self.build_tree(tree_01.right, None)
        else:
            root.val = tree_01.val + tree_02.val
            root.left = self.build_tree(tree_01.left, tree_02.left)
            root.right = self.build_tree(tree_01.right, tree_02.right)
        return root



if __name__ == '__main__':
    t1 = TreeNode(1)
    t1_3 = TreeNode(3)
    t1_3.left = TreeNode(5)
    t1.left = t1_3
    t1.right = TreeNode(2)

    t2 = TreeNode(2)
    t2_1 = TreeNode(1)
    t2_1.right = TreeNode(4)
    t2_3 = TreeNode(3)
    t2_3.right = TreeNode(7)
    t2.left = t2_1
    t2.right = t2_3

    solution = Solution()
    result = solution.mergeTrees(t1, t2)
    print(result)
    print('done')
