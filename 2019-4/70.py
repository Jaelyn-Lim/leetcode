# -*- coding: utf-8 -*-
# @Time    : 19-4-1 下午3:22
# @Author  : jaelyn
# @FileName: 70.py
# @Software: PyCharm
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
from functools import lru_cache

# lru_cache 在使用递归的时候，加上这个，可以大大减少计算次数


class Solution:
    # 渣渣递归超时
    @lru_cache()
    def climbStairs1(self, n: int) -> int:
        if n == 2:
            return 2
        elif n == 1:
            return 1
        return self.climbStairs1(n-1) + self.climbStairs1(n-2)

    # 来个动态规划，太占用空间，渣渣
    def climbStairs2(self, n: int) -> int:
        arr_list = [1, 2]
        for i in range(2, n):
            arr_list.append(arr_list[i-1] + arr_list[i-2])
        return arr_list[n-1]

    # 减少空间消耗的版本
    @lru_cache()
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        elif n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tem = a + b
            a = b
            b = tem
        return tem


if __name__ == '__main__':
    s = Solution()
    ans = s.climbStairs1(40)
    print(ans)

