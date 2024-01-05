class Solution(object):
    def numberOfBeams(self, bank):
        s=0
        p=bank[0].count("1")
        for i in range(1,len(bank)):
            c=bank[i].count("1")
            if c :
                s+=(p*c)
                p=c
        return s

        
        
