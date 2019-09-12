# -*- coding: utf-8 -*-
#
import heapq
class Solution(object):
    def negativify(self, n):
        n = -n
        return n

    def reorganizeString(self, S):
        res = ""
        heap = []
        heapq.heapify(heap)
        dic = {}
        for s in S:
            dic[s] = dic.get(s, 0) + 1

        for key, val in dic.items():
            heapq.heappush(heap, [self.negativify(val), key])

        # 最高频率的char超过总长一半，肯定会有相邻字符
        if heap[0][0] < -len(S) / 2:
            return ''

        while heap:
            tmp = heapq.heappop(heap)
            if heap and tmp[0] == heap[0][0]:
                tmp2 = heapq.heappop(heap)
                res += tmp2[1]
                tmp2[0] = tmp2[0] + 1
                heapq.heappush(heap, tmp)
                if tmp2[0] < 0:
                    heapq.heappush(heap, tmp2)
            else:
                res += tmp[1]
                tmp[0] = tmp[0] + 1
                if tmp[0] < 0:
                    heapq.heappush(heap, tmp)

        return res

test = Solution()
print test.reorganizeString("aab")
