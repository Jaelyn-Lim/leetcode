# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 23:17
# @Author  : jaelyn
# @FileName: 107.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        single_level = [root]
        ans = []
        while single_level:
            temp_single = []
            temp_ans = []
            for single in single_level:
                if single:
                    temp = single
                    temp_ans.append(temp.val)
                    if temp.left:
                        temp_single.append(temp.left)
                    if temp.right:
                        temp_single.append(temp.right)
            if temp_ans:
                ans.append(temp_ans)
            single_level = temp_single
        return ans[::-1]

        # 等比数列的前n项和 Sn = 2^n - 1
        # import math
        # max_level = int(math.log(len(root), 2)) + 1
        # ans = []
        # for i in range(max_level):
        #     level_ans = []
        #     temp = 2 ** i
        #     while temp:
        #         check = root.pop(0)
        #         if check:
        #             level_ans.append(check)
        #         temp -= 1
        #     ans.append(level_ans)
        # return ans[::-1]



if __name__ == '__main__':
    solution = Solution()
    # root = [3, 9, 20, None, None, 15, 7]
    tree20 = TreeNode(20)
    tree3 = TreeNode(3)
    tree3.left = TreeNode(9)
    tree3.right = tree20
    tree20.left = TreeNode(15)
    tree20.right = TreeNode(7)
    print(solution.levelOrderBottom(tree3))
