# -*- coding: utf-8 -*-
# @Time    : 2018/10/6 18:39
# @Author  : jaelyn
# @FileName: 762.py
# @Software: PyCharm

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime = [i+1 for i in range(20)]
        prime.pop(0)
        for num in range(20):
            for temp in range(num+1):
                o = num*temp
                if o == num or o == temp:
                    continue
                if o in prime:
                    prime.remove(o)
        ans = 0
        for num in range(L, R+1):
            temp = str(bin(num)).count('1')
            if temp in prime:
                ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    L = 6
    R = 10
    print(solution.countPrimeSetBits(L, R))
