# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 22:27
# @Author  : jaelyn
# @FileName: 13.py
# @Software: PyCharm

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        roman_num_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # lenght_s = len(s)
        for index, single_str in enumerate(s):
            ans += roman_num_dict[single_str]
        if 'IV' in s or 'IX' in s:
            ans -= 2
        if 'XL' in s or 'XC' in s:
            ans -= 20
        if 'CD' in s or 'CM' in s:
            ans -= 200
            # if single_str == "I":
            #     if index+1 < lenght_s:
            #         if s[index+1] == "V" or s[index+1] == "X":
            #             ans -= 2
            # if single_str == "X":
            #     if index+1 < lenght_s:
            #         if s[index+1] == "L" or s[index+1] == "C":
            #             ans -= 20
            # if single_str == "C":
            #     if index+1 < lenght_s:
            #         if s[index+1] == "D" or s[index+1] == "M":
            #             ans -= 200
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "MCMXCIV"
    print(solution.romanToInt(s))
