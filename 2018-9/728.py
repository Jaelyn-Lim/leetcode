# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 下午11:44
# @Author  : jaelyn
# @FileName: 728.py
# @Software: PyCharm


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        ans = []
        for i in range(left, right + 1):
            n = i
            flag = True
            while n > 0:
                w = n % 10
                if (w == 0) or (i % w != 0):
                    flag = False
                    break
                n //= 10
            if flag:
                ans.append(i)

        return (ans)

        # ans = []
        # for num in range(left, right+1):
        #     flag = True
        #     for n in str(num):
        #         if int(n) == 0 or num % int(n) != 0:
        #             flag = False
        #             break
        #     if flag:
        #         ans.append(num)
        # return ans


if __name__ == '__main__':
    solution = Solution()
    left = 1
    right = 22
    result = solution.selfDividingNumbers(left, right)
    print(result)