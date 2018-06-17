# -*- coding: utf-8 -*-
# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        dic = {}

        return self.isMatch(str, 0, pattern, 0, dic)

    def isMatch(self, str, i, pat, j, dic):
        if i == len(str) and j == len(pat):
            return True
        elif i == len(str):
            return False
        elif j == len(pat):
            return False

        if pat[j] in dic:
            curr = dic[pat[j]]
            # 比如当前pat是a，应该找red，结果发现剩下的str不是以red开头，果断false
            if not str.startswith(curr, i):
                return False
            else:
                # 继续找下一个match
                return self.isMatch(str, i + len(curr), pat, j + 1, dic)
        # 新的pattern单词, backtracking
        else:
            for k in range(i, len(str)):
                # 为新的pattern字母添加新对应的单词
                dic[pat[j]] = str[i:k + 1]
                if self.isMatch(str, k + 1, pat, j + 1, dic):
                    return True
                dic.pop(pat[j])

            return False

test = Solution()
print test.wordPatternMatch("aabb", "11112222")