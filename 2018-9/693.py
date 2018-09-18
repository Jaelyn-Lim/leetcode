# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 下午11:04
# @Author  : jaelyn
# @FileName: 693.py
# @Software: PyCharm

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_str = str(bin(n))
        if '11' in bin_str or '00' in bin_str:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    n = 7
    print(solution.hasAlternatingBits(n))