# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 下午11:27
# @Author  : jaelyn
# @FileName: 806.py
# @Software: PyCharm

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        x = 1
        l = 0
        for s in S:
            l += widths[ord(s)-97]
            if l > 100:
                x += 1
                l = widths[ord(s)-97]
        return [x, l]


if __name__ == '__main__':
    solution = Solution()
    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "abcdefghijklmnopqrstuvwxyz"
    print(solution.numberOfLines(widths, S))
