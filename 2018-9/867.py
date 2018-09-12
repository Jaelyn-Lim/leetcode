# -*- coding: utf-8 -*-
# @Time    : 2018/9/11 下午10:16
# @Author  : jaelyn
# @FileName: 867.py
# @Software: PyCharm


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # return list(map(list, zip(*A)))
        return list(zip(*A))


if __name__ == '__main__':
    solution = Solution()
    A = [[5],[8]]
    ret = solution.transpose(A)
    print(ret)