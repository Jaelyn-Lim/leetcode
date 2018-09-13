# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 下午11:12
# @Author  : jaelyn
# @FileName: 589.py
# @Software: PyCharm

# Definition for a Node.

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        pop: Remove and return item at index (default last).
        """
        if root is None:
            return []
        ret, q = [], [root]
        while q:
            node = q.pop()
            ret.append(node.val)
            if node.children:
                for child in node.children[::-1]:
                    if child:
                        q.append(child)
        return ret
        # if not root:
        #     return []
        # result = [root.val]
        # if not root.children:
        #     return result
        # for child in root.children:
        #     result += self.preorder(child)
        # return result


if __name__ == '__main__':
    solution = Solution()
    node5 = Node(5, None)
    node6 = Node(6, None)
    node3 = Node(3, [node5, node6])
    node2 = Node(2, None)
    node4 = Node(4, None)

    root = Node(1, [node3, node2, node4])
    ret = solution.preorder(root)
    print(ret)

