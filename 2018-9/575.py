# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 22:53
# @Author  : jaelyn
# @FileName: 575.py
# @Software: PyCharm

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        sister = set(candies)
        # for candy in candies:
        #     sister.add(candy)
        ans = len(sister)
        half_candles = len(candies)//2
        return ans if ans < half_candles else half_candles


if __name__ == '__main__':
    solution = Solution()
    candies = [1, 1, 2, 2, 3, 3]
    print(solution.distributeCandies(candies))