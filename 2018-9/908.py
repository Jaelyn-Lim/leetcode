# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 22:57
# @Author  : jaelyn
# @FileName: 908.py
# @Software: PyCharm

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2 * K)
        # min_a = min(A)
        # max_a = max(A)
        # ava_a = (max_a - min_a) / 2
        # return 0 if ava_a < K else max_a - min_a - 2 * K


if __name__ == '__main__':
    solution = Solution()
    A = [3,1,10]
    K = 4
    print(solution.smallestRangeI(A, K))

