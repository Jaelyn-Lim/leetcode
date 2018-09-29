# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 22:35
# @Author  : jaelyn
# @FileName: 429.py
# @Software: PyCharm

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
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
                    if temp.children:
                        temp_single.extend(temp.children)
            if temp_ans:
                ans.append(temp_ans)
            single_level = temp_single
        return ans

if __name__ == '__main__':
    solution = Solution()
    # 通用测试用的树
    node5 = Node(5, None)
    node6 = Node(6, None)
    node3 = Node(3, [node5, node6])
    node2 = Node(2, None)
    node4 = Node(4, None)
    root = Node(1, [node3, node2, node4])

    print(solution.levelOrder(root))

