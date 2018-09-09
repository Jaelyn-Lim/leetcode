# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 上午11:33
# @Author  : jaelyn
# @FileName: 476.py
# @Software: PyCharm

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num


if __name__ == '__main__':
    solution = Solution()
    num = 5
    print(solution.findComplement(num))