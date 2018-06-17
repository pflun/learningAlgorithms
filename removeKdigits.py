# -*- coding: utf-8 -*-
# 贪心，如果当前位比下一位大，就删除
class Solution(object):
    def removeKdigits(self, num, k):
        while k > 0:
            k -= 1
            for i in range(len(num)):
                if num[i] > num[i + 1]:
                    num = num[:i] + num[i + 1:]
                    break

        return str(int(num))

test = Solution()
print test.removeKdigits('1432219', 3)