# -*- coding: utf-8 -*-
# Queue
# 一秒很多个hit太占内存


class HitCounter(object):
    def __init__(self):
        self.q = []

    def hit(self, timestamp):
        self.q.append(timestamp)

    def getHits(self, timestamp):
        # in past 5 min
        while self.q and timestamp - self.q[0] >= 300:
            self.q.pop(0)

        return len(self.q)

test = HitCounter()
test.hit(1)
test.hit(2)
test.hit(3)
test.hit(300)
test.hit(301)
print test.getHits(301)

# https://www.youtube.com/watch?v=z9usYLTBKjY
# 两个数组，times[1] = 1 or 301 (timestamp % 300, 也就是301秒时把第一秒覆盖掉了), hits[1] = 1 or 2(同一时间hit两次)
# getHits O(300) = O(1)

import time

class HitCounter2(object):
    def __init__(self):
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self):
        curr = time.time()
        pos = int(curr) % 300
        self.times[pos] = int(curr)
        self.hits[pos] += 1

    def getHits(self):
        curr = time.time()
        res = 0
        for i in range(len(self.times)):
            if int(curr) - self.times[i] < 300:
                res += self.hits[i]

        return res

test2 = HitCounter2()
print test2.hit()
print test2.hit()
print test2.getHits()