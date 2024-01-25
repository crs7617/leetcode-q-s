class Solution:
    def isHappy(self, temp: int) -> bool:
        seen=set() 
        while(temp!= 1  and temp not in seen ):
            seen.add(temp)
            temp=sum(int(i)**2 for i in str(temp))
        return True if temp==1   else False
        
        
