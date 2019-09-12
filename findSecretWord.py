import random
# -*- coding: utf-8 -*-
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# 随机从wordlist选一个词A，guess一下，比如吻合4个，就更新wordlist把里面跟A吻合不是4的剔除（从而缩小集合）
class Master(object):
   def guess(self, word):
       """
       :type word: str
       :rtype int
       """
       secret = 'eiowzz'
       res = 0
       for i in range(len(secret)):
           if secret[i] == word[i]:
               res += 1
       return -1 if res == 0 else res

class Solution(object):
    def findSecretWord(self, wordlist, master):
        self.wordlist = wordlist

        # input two words
        def getDiff(w1, w2):
            res = 0
            for i in range(len(w1)):
                if w1[i] == w2[i]:
                    res += 1
            return -1 if res == 0 else res

        def helper():
            guessWord = random.choice(self.wordlist)
            matchNum = master.guess(guessWord)
            tmplist = []
            for w in self.wordlist:
                if getDiff(guessWord, w) == matchNum:
                    tmplist.append(w)
            self.wordlist = tmplist

        while len(self.wordlist) > 1:
            helper()

        return self.wordlist[0]

master = Master()
test = Solution()
print test.findSecretWord(["acckzz","ccbazz","eiowzz","abcczz"], master)