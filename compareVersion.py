# -*- coding: utf-8 -*-
class Solution(object):
    # incorrect
    def compareVersion(self, version1, version2):
        if not version1 or not version2:
            return 0
        v1 = version1.split('.')
        v2 = version2.split('.')
        # in case version1 = '1', v1 = ['1']
        if len(v1) == 1:
            v1.append(0)
        if len(v2) == 1:
            v2.append(0)
        # Compare
        if v1[0] > v2[0]:
            return 1
        elif v1[0] < v2[0]:
            return -1
        else:
            if v1[1] > v2[1]:
                return 1
            elif v1[1] < v2[1]:
                return -1
            else:
                return 0

    def compareVersion2(self, version1, version2):
        v1 = "".join(version1.split('.'))
        v2 = "".join(version2.split('.'))
        # 补全位数
        while len(v1) > len(v2):
            v2 += '0'
        while len(v2) > len(v1):
            v1 += '0'
        if v1 == v2:
            return 0
        elif v1 < v2:
            return -1
        elif v1 > v2:
            return 1

test = Solution()
print test.compareVersion2('0.1', '1')