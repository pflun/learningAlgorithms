class Solution(object):
    def checkSubarraySum(self, nums, k):
        preprocess = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for i in range(len(nums)):
            preprocess[i][i] = nums[i]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                preprocess[i][j] = preprocess[i][j - 1] + nums[j]
                if preprocess[i][j] % 6 == 0:
                    return True
        return False