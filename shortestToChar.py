# -*- coding: utf-8 -*-
# 先从左向右找右侧最近的C用find()，再从右向左找左侧最近的C（为了方便可以reverse），取两个list最小值
class Solution(object):
    def shortestToChar(self, S, C):
        n = len(S)
        left = [n] * n
        res = [n] * n

        for i in range(len(S)):
            idx = S[i:].find(C)
            # idx = -1 等于找不到
            if idx >= 0:
                left[i] = idx

        # 为了方便find，reverse string
        RS = S[::-1]
        for j in range(len(S)):
            idx = RS[j:].find(C)
            # 用向右向左的最小值更新res
            if idx >= 0:
                tmp = min(left[len(S) - j - 1], idx)
            else:
                tmp = left[len(S) - j - 1]

            res[len(S) - j - 1] = tmp

        return res


test = Solution()
print test.shortestToChar("loveleetcode", "e")