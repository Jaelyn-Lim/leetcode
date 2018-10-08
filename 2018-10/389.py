# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 23:43
# @Author  : jaelyn
# @FileName: 389.py
# @Software: PyCharm

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        ch = 0
        for c in s + t:
            ch ^= ord(c)
        return chr(ch)

        # for i in s:
        #     t = t.replace(i, "0", 1)
        #
        # for i in t:
        #     if i != '0':
        #         return i

if __name__ == '__main__':
    solution = Solution()
    s = "a"
    t = "aa"
    print(solution.findTheDifference(s, t))
