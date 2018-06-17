# -*- coding: utf-8 -*-
class PhoneDirectory(object):
    def __init__(self, maxnumber):
        self.queue = []
        self.used = set()
        self.maxnumber = maxnumber

        for i in range(maxnumber):
            self.queue.append(i)

    def get(self):
        if len(self.queue) == 0:
            return False
        else:
            res = self.queue.pop(0)
            self.used.add(res)

            return res

    def check(self, number):
        if number > self.maxnumber or number < 0:
            return False

        if number in self.used:
            return False
        else:
            return True

    def release(self, number):
        if number in self.used:
            self.used.remove(number)
            self.queue.append(number)

test = PhoneDirectory(3)
print test.get()
print test.get()
print test.check(2)
print test.get()
print test.check(2)
print test.release(2)
print test.check(2)

# root node的left child是一个bit，如果是1的话说明整个array的左半部分有available ID，0表示没有。
# right child表示右半边有没有available ID。这样一层层partition下去，最后bottom level就是代表整个0-max_id有没有被占用的bit array。
# 这样allocate就是O(n)，内存是原来bit array linear search方法的两倍。