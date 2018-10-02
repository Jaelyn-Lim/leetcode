# -*- coding: utf-8 -*-
# @Time    : 2018/10/2 21:14
# @Author  : jaelyn
# @FileName: 876.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_point = quick_point = head
        while slow_point and quick_point.next:
            if quick_point.next.next == None:
                return slow_point.next
            slow_point = slow_point.next
            quick_point = quick_point.next.next
        return slow_point

if __name__ == '__main__':
    solution = Solution()
    ans = ListNode(4)
    ans.next = ListNode(4)
    ans.next.next = ListNode(5)
    ans.next.next.next = ListNode(None)
    re = solution.middleNode(ans)

    while re:
        print(re.val)
        re = re.next

