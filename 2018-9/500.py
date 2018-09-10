# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 下午12:23
# @Author  : jaelyn
# @FileName: 500.py
# @Software: PyCharm

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        first_line = set("qwertyuiop")
        second_line = set("asdfghjkl")
        third_line = set("zxcvbnm")

        return list(filter(lambda word: set(word.lower()).issubset(first_line) or set(word.lower()).issubset(second_line) or set(word.lower()).issubset(third_line), words))

        # row1 = set("qwertyuiopQWERTYUIOP")
        # row2 = set("asdfghjklASDFGHJKL")
        # row3 = set("ZXCVBNMzxcvbnm")
        #
        # lst = list(filter(lambda x: set(x).issubset(row1) or set(x).issubset(row2) or set(x).issubset(row3), words))
        # return (lst)

        # issubset 子集

        # filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。


        # f_line = 'qwertyuiop'
        # s_line = 'asdfghjkl'
        # t_line = 'zxcvbnm'
        # res = []
        # for i in words:
        #     if all([x in f_line for x in i.lower()]) or all([x in s_line for x in i.lower()]) or all(
        #             [x in t_line for x in i.lower()]):
        #         res.append(i)
        # return res

        # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。

        # first_line = "qwertyuiop"
        # second_line = "asdfghjkl"
        # third_line = "zxcvbnm"
        # ans = []
        # for word in words:
        #     low_word = word.lower()
        #     for line in [first_line, second_line, third_line]:
        #         temp_flag = True
        #         for w in low_word:
        #             if w not in line:
        #                 temp_flag = False
        #                 continue
        #         if temp_flag:
        #             ans.append(word)
        # return ans


if __name__ == '__main__':
    solution = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    result = solution.findWords(words)
    print(result)