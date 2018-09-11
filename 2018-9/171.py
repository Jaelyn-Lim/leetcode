# -*- coding: utf-8 -*-
# @Time    : 2018/9/11 下午8:56
# @Author  : jaelyn
# @FileName: 171.py
# @Software: PyCharm


class Solution:
    def titleToNumber(self, s):
        """
        A:65 Z:90
        :type s: str
        :rtype: int
        """
        ans = 0
        for index, value in enumerate(s):
            ans += (ord(value)-64) * (26**(len(s)-index-1))
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "AAA"
    ret = solution.titleToNumber(s)
    print(ret)
