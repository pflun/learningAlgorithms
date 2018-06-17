# -*- coding: utf-8 -*-
# isFileDone
# merge interval
# 给一堆 Chunk 和一个 file size,问给定的一堆 Chunk 能不能组成 complete file.
# Chunk 就是一个左开右闭的区间, 如[0, 4)表示这个 chunk 包含 0, 1, 2, 3 这 4 个 byte. 给定的 size 是
# 这个文件大小.
# boolean isCompleteFile(List<Chunk> chunks, int size)
# 例如:
# chunks = [[0, 1), [1, 3), [3, 4)] size = 4 => 结果是 true
# chunks = [[0, 1), [1, 3), [3, 4)] size = 5 => 结果是 false chunks = [[0, 1), [2, 3), [3, 4)] size = 4 => 结果是 false

# class Chunk(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def isFileDone(self, chunks, size):
        res = []
        chunks = sorted(chunks, key=lambda x: x[0])
        for chunk in chunks:
            # first interval or no overlap
            if len(res) == 0 or res[-1][1] < chunk[0]:
                res.append(chunk)
            else:
                # update last interval
                res[-1][1] = max(res[-1][1], chunk[1])

        if len(res) == 1:
            if res[0][0] == 0 and res[0][1] == size:
                return True
            else:
                return False
        else:
            return False

test = Solution()
print test.isFileDone([[0,1],[2,3],[3,4]], 4)