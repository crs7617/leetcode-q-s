class Solution(object):
    def findJudge(self, n, trust):
        trustcount = [0] * (n + 1) 

        for relation in trust:
            trustcount[relation[0]] -= 1
            trustcount[relation[1]] += 1

        for i in range(1, n + 1):
            if trustcount[i] == n - 1:
                return i

        return -1  
