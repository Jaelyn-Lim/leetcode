# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 下午10:59
# @Author  : jaelyn
# @FileName: 521.py
# @Software: PyCharm

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))
        # if a == b:
        #     return -1
        # elif len(a) == len(b):
        #     return len(a)
        # return len(a) if len(a) > len(b) else len(b)



if __name__ == '__main__':
    solution = Solution()
    a = "aba"
    b = "cdc"
    print(solution.findLUSlength(a, b))
