class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count_in_t = defaultdict(int)
        for char in t:
            char_count_in_t[char] += 1
        
        i = 0  
        j = 0  
        
        required_chars = len(t)
        
        min_start = 0
        min_length = float('inf')  
        
        while j < len(s):
            if char_count_in_t[s[j]] > 0:
                required_chars -= 1  
            
            char_count_in_t[s[j]] -= 1  
            j += 1  
            
            while required_chars == 0:
                if j - i < min_length:
                    min_start = i
                    min_length = j - i
                
                char_count_in_t[s[i]] += 1 

                if char_count_in_t[s[i]] > 0:
                    required_chars += 1
                
                i += 1  
        
        return s[min_start:min_start + min_length] if min_length != float('inf') else ""
