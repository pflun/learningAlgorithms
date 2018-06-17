# -*- coding: utf-8 -*-
#
import random
class Solution(object):
    def weightedRandom(self, objects, probabilities):
        if len(objects) != len(probabilities):
            return
        revisedP = []

        for i in range(len(probabilities)):
            for _ in range(probabilities[i]):
                revisedP.append(objects[i])

        index = random.randint(0, len(revisedP) - 1)

        return revisedP[index]


test = Solution()
print test.weightedRandom(['a','b','c','d'], [1,2,3,4])