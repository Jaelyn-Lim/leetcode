
# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 下午11:01
# @Author  : jaelyn
# @FileName: 258'.py
# @Software: PyCharm

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        return (num - 1) % 9 + 1 if num > 0 else 0

        # if num < 10:
        #     return num
        # ans = 0
        # for n in str(num):
        #     ans += int(n)
        # return self.addDigits(ans)


if __name__ == '__main__':
    solution = Solution()
    num = 38
    ret = solution.addDigits(num)
    print(ret)