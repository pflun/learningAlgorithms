# -*- coding: utf-8 -*-
class Solution(object):
    # TLE
    def minSwap(self, A, B):
        if len(A) == 1:
            return 0

        self.res = float('inf')

        def helper(A, B, index, step):
            # 剪枝
            if index == len(A) or step >= self.res:
                return

            if self.isIncrease(A) and self.isIncrease(B):
                self.res = min(self.res, step)
                return

            for i in range(index, len(A)):
                A[i], B[i] = B[i], A[i]
                helper(A, B, index + 1, step + 1)
                A[i], B[i] = B[i], A[i]

        helper(A, B, 0, 0)

        return self.res

    def isIncrease(self, arr):
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False

        return True

test = Solution()
print test.minSwap([0,7,8,10,10,11,12,13,19,18],[4,4,5,7,11,14,15,16,17,20])