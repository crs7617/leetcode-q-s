class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dp(i, j, moves):
            if i < 0 or j < 0 or i == m or j == n:
                return 1
            if moves == 0:
                return 0
            return sum(
                [
                    dp(i - 1, j, moves - 1),
                    dp(i + 1, j, moves - 1),
                    dp(i, j - 1, moves - 1),
                    dp(i, j + 1, moves - 1),
                ]
            ) % (10 ** 9 + 7)

        return dp(startRow, startColumn, maxMove)
        
