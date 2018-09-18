# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 下午10:10
# @Author  : jaelyn
# @FileName: 905.py
# @Software: PyCharm

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_elements = []
        odd_elements = []
        for a in A:
            if a % 2 == 0:
                even_elements.append(a)
            else:
                odd_elements.append(a)
        return even_elements + odd_elements

if __name__ == '__main__':
    solution = Solution()
    a = [3, 1, 2, 4]
    ret = solution.sortArrayByParity(a)
    print(ret)