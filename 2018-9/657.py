# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 上午11:24
# @Author  : jaelyn
# @FileName: 657.py
# @Software: PyCharm

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")

if __name__ == '__main__':
    solution = Solution()
    input_str = "UUUDDDLLLRRR"
    results = solution.judgeCircle(input_str)
    print(results)