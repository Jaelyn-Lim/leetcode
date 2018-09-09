# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 上午11:37
# @Author  : jaelyn
# @FileName: 852.py
# @Software: PyCharm

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))


if __name__ == '__main__':
    solution = Solution()
    a = [0, 2, 1, 0]
    result = solution.peakIndexInMountainArray(a)
    print(result)