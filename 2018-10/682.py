# -*- coding: utf-8 -*-
# @Time    : 2018/10/6 19:08
# @Author  : jaelyn
# @FileName: 682.py
# @Software: PyCharm

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans_list = []
        for num in ops:
            if num == "C":
                ans_list.pop()
            elif num == "D":
                ans_list.append(ans_list[len(ans_list)-1]*2)
            elif num == "+":
                ans_list.append(ans_list[len(ans_list)-1]+ans_list[len(ans_list)-2])
            else:
                ans_list.append(int(num))
        return sum(ans_list)



if __name__ == '__main__':
    solution = Solution()
    # o = ["5","-2","4","C","D","9","+","+"]
    o = ["5","2","C","D","+"]
    print(solution.calPoints(o))
