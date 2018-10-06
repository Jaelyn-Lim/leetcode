# -*- coding: utf-8 -*-
# @Time    : 2018/10/6 16:25
# @Author  : jaelyn
# @FileName: 637.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        root_list, ans = [root], []
        while root_list:
            temp = 0
            temp_list = []
            for i in root_list:
                temp += i.val
                if i.right:
                    temp_list.append(i.right)
                if i.left:
                    temp_list.append(i.left)
            ans.append(temp/float(len(root_list)))
            root_list = temp_list
        return ans


if __name__ == '__main__':
    solution = Solution()

    t3 = TreeNode(3)
    t3.left = TreeNode(9)
    t20 = TreeNode(20)
    t20.left = TreeNode(15)
    t20.right = TreeNode(7)
    t3.right = t20

    print(solution.averageOfLevels(t3))
