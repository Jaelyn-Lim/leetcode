# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午4:53
# @Author  : jaelyn
# @FileName: 804.py
# @Software: PyCharm

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ret_set = set()
        for word in words:
            morse_word = str("".join(list(words_morse[ord(w)-97] for w in word)))
            # print(morse_word)
            ret_set.add(morse_word)
        return len(ret_set)


if __name__ == '__main__':
    solution = Solution()
    words = ["gin", "zen", "gig", "msg"]
    result = solution.uniqueMorseRepresentations(words)
    print(result)
