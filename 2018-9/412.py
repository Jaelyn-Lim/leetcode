# -*- coding: utf-8 -*-
# @Time    : 2018/9/23 11:28
# @Author  : jaelyn
# @FileName: 412.py
# @Software: PyCharm

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        f = "Fizz"
        b = "Buzz"
        ans = []
        for i in range(n):
            index = i+1
            app = ""
            if index % 3 == 0:
                app += f
            if index % 5 == 0:
                app += b
            if not app:
                app += str(index)
            ans.append(app)
        return ans


if __name__ == '__main__':
    solution = Solution()
    n = 15
    print(solution.fizzBuzz(n))