# -*- coding: utf-8 -*-
# https://discuss.leetcode.com/topic/27098/python-solution-easy-to-understand
# 两部pass，先用 2／3 表示下一步活／死，再变回01
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]], int = 0 dead,1 live
        " 2 dead -> live ; 3 live -> dead
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        if m == 0 or n == 0:
            return
        for iM in range(m):
            for iN in range(n):
                numNeighbor = sum([board[i][j]%2 for i in range(iM-1,iM+2) for j in range(iN-1,iN+2) if 0 <= i < m and 0<= j < n]) - board[iM][iN]
                if board[iM][iN] == 0 and numNeighbor == 3:
                    board[iM][iN] = 2
                if board[iM][iN] == 1 and ( numNeighbor < 2 or numNeighbor >  3):
                    board[iM][iN] = 3
        for iM in range(m):
            for iN in range(n):
                if board[iM][iN] == 2:
                    board[iM][iN] = 1
                if board[iM][iN] == 3:
                    board[iM][iN] = 0

    def gameOfLife2(self, board):

        def helper(board, y, x):
            res = 0
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]

            for d in dir:
                curry = y + d[0]
                currx = x + d[1]
                if curry < 0 or curry == len(board) or currx < 0 or currx == len(board[0]):
                    continue
                if board[curry][currx] == 1 or board[curry][currx] == 3:
                    res += 1

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                live = helper(board, i, j)
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 3
                elif board[i][j] == 0:
                    if live == 3:
                        board[i][j] = 2

        # 3 => 0, 2 => 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

        # don't need to return, modify in-place
        return board

test = Solution()
print test.gameOfLife2(
 [[0,0,1,0],
  [0,1,1,0],
  [0,0,0,1]])