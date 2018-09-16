# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 下午5:23
# @Author  : jaelyn
# @FileName: 590.py
# @Software: PyCharm

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # res = []
        # if root == None: return res
        #
        # stack = [root]
        # while stack:
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     if curr.children:
        #         stack.extend(curr.children)
        #
        # return res[::-1]
        if root is None:
            return []
        ret, q = [], [root]
        while q:
            node = q.pop()
            if node.children:
                for child in node.children:
                    if child:
                        q.append(child)
            ret.append(node.val)
        return ret[::-1]
        # if not root:
        #     return []
        # result = []
        # if not root.children:
        #     return [root.val]
        # for child in root.children:
        #     result += self.postorder(child)
        # result += [root.val]
        # return result


if __name__ == '__main__':
    solution = Solution()
    node5 = Node(5, None)
    node6 = Node(6, None)
    node3 = Node(3, [node5, node6])
    node2 = Node(2, None)
    node4 = Node(4, None)

    root = Node(1, [node3, node2, node4])
    ret = solution.postorder(root)
    print(ret)