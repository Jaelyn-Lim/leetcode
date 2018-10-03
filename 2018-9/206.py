# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 23:35
# @Author  : jaelyn
# @FileName: 206.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head is not None:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre


if __name__ == '__main__':
    solution = Solution()
    # 1->2->3->4->5->NULL
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    ret = solution.reverseList(l1)
    while ret:
        print(ret.val)
        ret = ret.next