class Solution:
    def findWinners(self, matches):
        l = [0] * 100001

        for winner, loser in matches:
            if l[winner] == 0:
                l[winner] = -1

            if l[loser] == -1:
                l[loser] = 1
            else:
                l[loser] += 1

        zero = [i for i in range(1, 100001) if l[i] == -1]
        one = [i for i in range(1, 100001) if l[i] == 1]

        return [zero, one]
