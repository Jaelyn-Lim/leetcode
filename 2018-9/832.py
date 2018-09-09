# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 上午11:49
# @Author  : jaelyn
# @FileName: 832.py
# @Software: PyCharm

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for index, a in enumerate(A):
            a = a[::-1]
            a = [int(i != 1) for i in a]
            A[index] = a
        return A

        # result = []
        # for line in A:
        #     line = line[::-1]
        #     result.append(list(map(lambda a: int(a != 1), line)))
        # return result


if __name__ == '__main__':
    solution = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    result = solution.flipAndInvertImage(A)
    print(result)