# -*- coding: utf-8 -*-
# Dropbox-highestMinimumSharpness
# Given a 2-d array of "sharpness" values. Find a path from the leftmost column to the rightmost column which has the highest minimum sharpness.
# Output the highest minimum sharpness. Each move can only move to the top right, right or bottom right grid.
# Example: 3*3 matrix
# 5 7 2
# 7 5 8
# 9 1 5
# The path with highest minimum sharpness is 7-->7-->8, because 7 is the highest minimum value in all the paths.
# Idea: Use DP dp[r][c] = min(max(dp[r-1][c-1], dp[r][c-1], dp[r+1][c-1]), grid[r][c])

class Solution(object):
    def highestMinimumSharpness(self, board):
        rows, cols = len(board), len(board[0])
        for c in xrange(1, cols):
            for r in xrange(rows):
                # 初始值是同一行前一列（上次求得的最小值）
                lmax = board[r][c - 1]
                # 第一行和最后一行的corner case
                if r - 1 >= 0:
                    lmax = max(lmax, board[r - 1][c - 1])
                if r + 1 < rows:
                    lmax = max(lmax, board[r + 1][c - 1])
                board[r][c] = min(board[r][c], lmax)
        res = board[0][-1]
        print board, res
        for r in xrange(1, rows):
            res = max(res, board[r][-1])
        return res

test = Solution()
print test.highestMinimumSharpness(
    [[5,7,2],
     [7,5,8],
     [9,1,5]])
print test.highestMinimumSharpness(
    [[1,2,3,9],
     [8,6,10,8],
     [9,4,11,12]])