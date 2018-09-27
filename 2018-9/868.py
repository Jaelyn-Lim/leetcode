# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 21:39
# @Author  : jaelyn
# @FileName: 868.py
# @Software: PyCharm

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        A = []
        for i in range(32):
            temp = (N >> i) & 1
            # print(temp, bin(temp))
            if temp:
                A.append(i)
            # print(temp)
            # temp2 = temp #& 1
            # print(temp2)
            # if temp2:
            #     A.append(i)
        # A = [i for i in range(32) if (N >> i) & 1]
        # print(A)

        ans = 0
        str_binary = str(bin(N))[2:]
        str_binary_list = str_binary.split('1')
        for i in str_binary_list[1:len(str_binary_list)-1]:
            temp = len(i) + 1
            if temp > ans:
                ans = temp
        return ans



if __name__ == '__main__':
    solution = Solution()
    n = 22
    print(solution.binaryGap(n))
