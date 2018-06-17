# -*- coding: utf-8 -*-
# 在字符串中找出数字，并输出，例如 12ABC45 输出{12, 45}.

class Solution(object):
    def findNum(self, s):
        res = []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = int(s[i])
                # 识别比如123
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1

                res.append(num)
            i += 1

        return res

test = Solution()
print test.findNum('12ABC45')