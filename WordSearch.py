# Time Complexity : O(m * n * 4^L) where L = word.length()
# Space Complexity : O(L) recursion stack in the worst case.
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Approach : We go cell by cell and start DFS if the first character matches.
# We mark visited cells as # to avoid reuse during the same path.
# If we match all characters, we return true, else we backtrack.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dirs = [[0,-1], [0, 1], [-1, 0], [1,0]]
        self.rows, self.cols = len(board), len(board[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    
    def dfs(self, board: List[List[str]], i: int, j: int, word: str, idx: int) -> bool:
        if idx == len(word):
            return True

        if i < 0 or j < 0 or i == self.rows or j == self.cols or board[i][j] == '#':
            return False

        if board[i][j] != word[idx]:
            return False

        board[i][j] = "#"

        for dx, dy in self.dirs:
            r = dx + i
            c = dy + j

            if self.dfs(board, r, c, word, idx + 1):
                return True

        board[i][j] = word[idx]

        return False

        