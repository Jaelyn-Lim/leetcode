# -*- coding: utf-8 -*-
# @Time    : 2018/9/23 10:27
# @Author  : jaelyn
# @FileName: 371.py
# @Software: PyCharm

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])


if __name__ == '__main__':
    solution = Solution()
    a = 1
    b = 2
    print(solution.getSum(a, b))