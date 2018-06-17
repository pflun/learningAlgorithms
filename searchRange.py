# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=NlLP8Op_4zw
class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        res = []

        # Search left
        while left + 1 < right:
            mid = (left + right) / 2
            # 找左端时，即使找到target也移动右指针，画图就看明白了
            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            res.append(left)
        elif nums[right] == target:
            res.append(right)
        else:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        # Search right
        while left + 1 < right:
            mid = (left + right) / 2
            # 找右端时，即使找到target也移动左指针
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        if nums[left] == target:
            res.append(left)
        elif nums[right] == target:
            res.append(right)

        return res


test = Solution()
print test.searchRange([5, 7, 7, 8, 8, 8, 10], 8)