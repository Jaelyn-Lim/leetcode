# -*- coding: utf-8 -*-
# @Time    : 2018/10/6 19:26
# @Author  : jaelyn
# @FileName: 169.py
# @Software: PyCharm


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]

        # from collections import Counter
        # word_counts = Counter(nums)
        # # 出现频率最高的3个单词
        # top_three = word_counts.most_common(1)
        # return top_three[0][0]


if __name__ == '__main__':
    solution = Solution()
    n = [2, 2, 1, 1, 1, 2, 2]
    print(solution.majorityElement(n))
