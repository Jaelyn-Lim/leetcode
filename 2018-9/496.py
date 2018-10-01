# -*- coding: utf-8 -*-
# @Time    : 2018/10/1 21:52
# @Author  : jaelyn
# @FileName: 496.py
# @Software: PyCharm

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dic, stack = {}, []
        for number in nums2:
            while stack and stack[-1] < number:
                dic[stack.pop()] = number
            stack.append(number)
        return [dic.get(i, -1) for i in nums1]
        
        # ans = []
        # for f in findNums:
        #     flag = True
        #     if f in nums:
        #         index = nums.index(f)
        #         while index < len(nums):
        #             if nums[index] > f:
        #                 flag = False
        #                 ans.append(nums[index])
        #                 break
        #             index += 1
        #     if flag:
        #         ans.append(-1)
        # return ans



if __name__ == '__main__':
    solution = Solution()
    # nums1 = [4, 1, 2]
    # nums2 = [1, 3, 4, 2]
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(solution.nextGreaterElement(nums1, nums2))
