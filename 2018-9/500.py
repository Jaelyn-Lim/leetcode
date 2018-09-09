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
        first_line = "qwertyuiop"
        second_line = "asdfghjkl"
        third_line = "zxcvbnm"
        for word in words:
            pass


if __name__ == '__main__':
    solution = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    result = solution.findWords(words)
    print(result)