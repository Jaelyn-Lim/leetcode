# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午12:00
# @Author  : jaelyn
# @FileName: 461.py
# @Software: PyCharm


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        return str(bin(x ^ y)).count("1")



        # result = 0
        # a = x ^ y
        # while a > 0:
        #     if a % 2 == 1:
        #         result += 1
        #     a //= 2
        # return result

        # ans = 0
        # x_b = str(bin(x)).replace("0b", "")
        # y_b = str(bin(y)).replace("0b", "")
        # if len(x_b) > len(y_b):
        #     y_b = "0"*(len(x_b)-len(y_b)) + y_b
        # elif len(x_b) < len(y_b):
        #     x_b = "0"*(len(y_b)-len(x_b)) + x_b
        # for x_str, y_str in zip(x_b, y_b):
        #     if x_str != y_str:
        #         ans += 1
        # return ans


if __name__ == '__main__':
    s = Solution()
    x = 1
    y = 4
    ret = s.hammingDistance(x, y)
    print(ret)