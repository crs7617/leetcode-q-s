class Solution:
    def cherryPickup(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])

        @cache
        def f(i, j, y):
            if i != m and 0 <= j < y < n:
                result = 0
                for p in (-1, 0, 1):
                    for q in (-1, 0, 1):
                        result = max(result, f(i+1, j+p, y+q))
            
                result += g[i][j] + g[i][y]

                return result

            return 0

        return f(0, 0, n-1)
