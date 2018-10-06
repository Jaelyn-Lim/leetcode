# -*- coding: utf-8 -*-
# @Time    : 2018/10/6 19:36
# @Author  : jaelyn
# @FileName: 9.py
# @Software: PyCharm

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)


if __name__ == '__main__':
    solution = Solution()
    n = -121
    print(solution.isPalindrome(n))
