# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=Q4i_rqON2-E
# 递归, 'abbc' and 'acc' 最右相等，同时删除最右传入下一递归；'abb' and 'ac' = 1 + min(D('ab', 'ac')添加b, D('abb', 'a')添加c, D('ab', 'a')同时添加b c)
# 出口：其中一个input为0，step就是另一个input的长度；两个都为0，step就是0

class Solution(object):
    def minDistance(self, word1, word2):
        if len(word1) == 0 and len(word2) == 0:
            return 0
        elif len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)

        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:-1], word2[:-1])

        c1 = self.minDistance(word1[:-1], word2)
        c2 = self.minDistance(word1, word2[:-1])
        c3 = self.minDistance(word1[:-1], word2[:-1])

        curr = 1 + self.minThree(c1, c2, c3)

        return curr

    def minThree(self, c1, c2, c3):
        res = min(c1, c2)

        res = min(res, c3)

        return res


test = Solution()
print test.minDistance('ab', 'a')