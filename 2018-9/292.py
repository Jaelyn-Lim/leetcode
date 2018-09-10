# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 下午11:14
# @Author  : jaelyn
# @FileName: 292.py
# @Software: PyCharm

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n <= 3:
        #     return True
        return n % 4 != 0


if __name__ == '__main__':
    solution = Solution()
    n = 1
    ret = solution.canWinNim(n)
    print(ret)