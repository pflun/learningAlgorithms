# -*- coding: utf-8 -*-
# 突然发现这题不需要走到左上角(右下角)，AT是下边和右边，PA是上边和左边
# 而且也不需要 originX(ox) (oy)，流到一个cell高度就是那个cell
# 题目poorly worded，另外这题BFS也能解
# 没难度，就不继续改了

class Solution(object):
    def pacificAtlantic(self, matrix):
        self.res = []
        self.pa = []
        self.at = []

        def canReach(dx, dy, ox, oy, cx, cy, visited):
            if cx < 0 or cx == len(matrix[0]) or cy < 0 or cy == len(matrix) or (cx, cy) in visited:
                return
            visited.add((cx, cy))

            if cx == dx and cy == dy:
                if dx == 0 and dy == 0:
                    self.pa.append([oy, ox])
                elif dx == len(matrix[0]) - 1 and dy == len(matrix) - 1:
                    self.at.append([oy, ox])

            if matrix[oy][ox] < matrix[cy][cx]:
                return

            dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            for d in dir:
                canReach(dx, dy, ox, oy, cx + d[0], cy + d[1], visited)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited = set()
                canReach(0, 0, i, j, i, j, visited)
                visited = set()
                canReach(len(matrix[0]) - 1, len(matrix) - 1, i, j, i, j, visited)

        return self.pa

test = Solution()
print test.pacificAtlantic([
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
])
