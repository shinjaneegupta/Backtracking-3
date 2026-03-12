# Time Complexity : O(n * n!)
# Space Complexity : O( n^2 ) for the board + O( n ) recursive stack space
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Approach : We’re placing queens row by row and checking if each placement is safe.
# If it's valid, we place it and move to the next row recursively.
# When all rows are filled, we convert the board to a list and store it in the result.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [[False]*n for _ in range(n)]
        self.helper(board, 0, n)
        return self.res

    def helper(self, board, row, n):
        if row == n:
            temp = []
            for i in range(n):
                sb = []
                for j in range(n):
                    if board[i][j]:
                        sb.append("Q")
                    else:
                        sb.append(".")
                temp.append("".join(sb))
            self.res.append(temp)
            return

        for j in range(n):
            if self.isValid(board, row, j, n):
                board[row][j] = True
                self.helper(board, row+1, n)
                board[row][j] = False

    def isValid(self, board, i, j, n):
        r,c = i, j
        while r >= 0:
            if board[r][c]:
                return False
            r -= 1

        r,c = i, j
        while r >= 0 and c >= 0:
            if board[r][c]:
                return False
            r -= 1
            c -= 1

        r,c = i, j
        while r >= 0 and c < n:
            if board[r][c]:
                return False
            r -= 1
            c += 1

        return True


        
        