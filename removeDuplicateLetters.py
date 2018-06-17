# -*- coding: utf-8 -*-
# The basic idea is to find out the smallest result letter by letter (one letter at a time). Here is the thinking process for input "cbacdcbc":
#
# find out the last appeared position for each letter;
# c - 7
# b - 6
# a - 2
# d - 4
# find out the smallest index from the map in step 1 (a - 2);
# the first letter in the final result must be the smallest letter from index 0 to index 2;
# repeat step 2 to 3 to find out remaining letters.
# the smallest letter from index 0 to index 2: a
# the smallest letter from index 3 to index 4: c
# the smallest letter from index 4 to index 4: d
# the smallest letter from index 5 to index 6: b
# so the result is "acdb"

class Solution(object):
    def removeDuplicateLetters(self, s):
        # 存最后一次出现的位置
        self.dic = {}
        self.res = ''

        for i in range(len(s)):
            self.dic[s[i]] = i

        self.length = len(self.dic)
        lIndex = 0

        for _ in range(self.length):
            rIndex = self.findSmallest(self.dic, lIndex)
            # smallidx表示这次循环最小的字母的位置
            smallidx = lIndex
            for i in range(lIndex, rIndex + 1):
                if s[i] < s[smallidx]:
                    smallidx = i

            self.res += s[smallidx]
            # 左指针移到这次最小位置的右边
            lIndex = smallidx + 1

        return self.res

    # 找大于左指针的最小index
    def findSmallest(self, dic, lIndex):
        res = float('inf')
        for i in dic.values():
            if res > i and i >= lIndex:
                res = i

        return res

test = Solution()
print test.removeDuplicateLetters("cbacdcbc")