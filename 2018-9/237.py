# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 下午10:45
# @Author  : jaelyn
# @FileName: 237.py
# @Software: PyCharm

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
