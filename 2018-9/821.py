# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 下午10:26
# @Author  : jaelyn
# @FileName: 821.py
# @Software: PyCharm

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ans_list = []
        for i in range(len(S)):
            left, right = S[i - len(S)::-1].find(C), S[i:].find(C)
            if left == -1:
                left = 10000
            if right == -1:
                right = 10000
            ans_list.append(min(left, right))
        return ans_list
        # ans_list = []
        # for index, s_c in enumerate(S.split(C)):
        #     if index == 0:
        #         for i in range(len(s_c)):
        #             ans_list.append((len(s_c)-i))
        #     elif index == len(s_c)-1:
        #         pass
        #     else:
        #         for i in range(len(s_c)//2):
        #             ans_list.append(i+1)
        #         if len(s_c) % 2 != 0:
        #             ans_list.append(len(s_c)//2+1)
        #         for i in range(len(s_c)//2):
        #             ans_list.append((len(s_c)//2)-i)
        #     ans_list.append(0)
        #     print(index, s_c)
        # ans_list.pop()
        # return ans_list


if __name__ == '__main__':
    solution = Solution()
    S = "abaa"
    C = 'b'
    ret = solution.shortestToChar(S, C)
    print(ret)