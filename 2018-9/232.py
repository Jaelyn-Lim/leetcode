# -*- coding: utf-8 -*-
# @Time    : 2018/10/2 20:40
# @Author  : jaelyn
# @FileName: 232.py
# @Software: PyCharm

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_list = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue_list.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue_list.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue_list[0]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue_list) == 0

# Your MyQueue object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyQueue()
    x = 1
    obj.push(x)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()
    print(param_2)
    # param_3 = obj.peek()
    param_4 = obj.empty()

