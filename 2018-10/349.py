# -*- coding: utf-8 -*-
# @Time    : 2018/10/6 17:13
# @Author  : jaelyn
# @FileName: 349.py
# @Software: PyCharm

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    solution = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(solution.intersection(nums1, nums2))