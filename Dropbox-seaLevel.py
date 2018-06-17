# -*- coding: utf-8 -*-
# You’re given an elevation map for a rectangular area of land. The map is represented by 2-D array of numbers where each cell contains the elevation above sea level of the corresponding area of the map.
# You need a path that connects the west edge of the map with the east edge of the map. Starting at the west edge of the map you can only move in single cell steps east, southeast, or northeast..
# You need to find how much can the sea level rise before submerging all such paths. Write a function that takes in a 2-D array and returns a single number
# 例子：
# west         east
# ----------------- north
# | 1 | 2 | 3 | 9 |.
# -----------------
# | 8 | 6 | 10 | 8 |
# -----------------.
# | 9 | 4| 11| 12|
# -----------------  south// sea=6
# DP
# 起始可以是第一列中任何一个位置，向右边走的时候可以是右边，右上，右下，3个cell。 水位从0开始，每走一步就上升1，水没过的path不能走了。
# 然后问找一个路径，让整条路径的是高的海拔的value最小。比如说：
# 3124
# 5718
# 3926.
# 3 -> 1 -> 2 -> 4 是一条valid的路径，3-> 7-> 2-> 4也是一条valid的路径，但是第一条中最大值是4，而第二条中最大值是7。那么返回4

class Solution(object):
    def seaLevel(self, board):
        rows, cols = len(board), len(board[0])
        water = 0
        for c in xrange(1, cols):
            water += 1
            for r in xrange(rows):
                if board[r][c] < water:
                    board[r][c] = float('inf')
                    break
                # 初始值是同一行前一列（上次求得的最小值）
                left_min = board[r][c - 1]
                # 第一行和最后一行的corner case
                if r - 1 >= 0:
                    left_min = min(left_min, board[r - 1][c - 1])
                if r + 1 < rows:
                    left_min = min(left_min, board[r + 1][c - 1])
                board[r][c] = max(board[r][c], left_min)
        res = board[0][-1]
        print board, res
        for r in xrange(1, rows):
            res = min(res, board[r][-1])
        return res

test = Solution()
print test.seaLevel(
    [[3,1,2,4],
     [5,7,1,8],
     [3,9,2,6]])
