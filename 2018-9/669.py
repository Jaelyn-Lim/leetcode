# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 22:20
# @Author  : jaelyn
# @FileName: 669.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        二叉搜索树： 左<根<右
        在遍历的时候就需要修改树的结构，去除不需要的节点
        所以对于 根<左 的时候，说明左边的节点不满足，需要去除，就直接返回改节点右边修改好之后的节点
        当 根>右 的时候，就需要将左边的修改之后的节点返回
        最后如果当前的节点满足大小的话
        就将改节点的左边重新赋值为修改好之后的左边的节点
        将节点右边的节点赋值为修改好之后的右边的节点
        就这样一层层递归获得结果

        对于之所以返回子节点的原因
        对于一些要去除的节点来说，在递归中直接返回自己的子节点就是最好的去除方式
        不过这个时候就需要考虑是需要去除哪个节点。
        根据搜索二叉树的性质，左边的一定会比右边的子节点小，左<根<右
        又因为所获取的值 根 < L ，这个时候如果返回左边的节点话，也就是只能拿到更小的值，一样也不满足条件
        所以就直接返回右边比较大的值
        并且按照二叉树的性质，左半边的所有值也一定会比根节点值要小，也就是说左半边的所有节点其实也是不满足的，可以直接去除一整个左半边

        去除右边同理
        """
        if not root:
            return None
        temp = root.val
        if temp < L:
            return self.trimBST(root.right, L, R)
        if temp > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node2.left = node1

    node0 = TreeNode(0)
    node0.right = node2

    node4 = TreeNode(4)
    node3 = TreeNode(3)
    node3.left = node0
    node3.right = node4

    solution = Solution()
    L = 1
    R = 3
    ans = solution.trimBST(node3, L, R)
    print(ans)
