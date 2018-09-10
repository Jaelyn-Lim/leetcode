# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 上午12:01
# @Author  : jaelyn
# @FileName: 557.py
# @Software: PyCharm

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return ' '.join(s.split(' ')[::-1])[::-1]

        # ans = []
        # for single_word in s.split(' '):
        #     ans.append(single_word[::-1])
        # return ' '.join(ans)


if __name__ == '__main__':
    solu = Solution()
    s = "Let's take LeetCode contest"
    ret = solu.reverseWords(s)
    print(ret)
