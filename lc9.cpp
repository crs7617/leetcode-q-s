class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }

        long reversed=0;
        long temp=x;

        while(temp!=0){
            int d=temp%10;
            reversed=reversed*10 + d;
            temp/=10;
        }

        return (reversed==x);
        
    }
};
