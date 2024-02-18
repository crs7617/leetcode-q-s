class Solution:
    def mostBooked(self, n: int, m: List[List[int]]) -> int:
        r, c = [0]*n, [0]*n # rooms, counter
        for s, e in sorted(m):
            found = 0
            for i,f in enumerate(r):
                if f <= s:
                    r[i] = e
                    c[i] += 1
                    found = 1
                    break

            if not found:
                q = r.index(min(r))
                r[q] += e-s
                c[q] += 1

        return c.index(max(c))
