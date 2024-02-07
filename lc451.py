class Solution:
    def frequencySort(self, s: str) -> str:
        
        char_count = Counter(s)
        sorted_chars = sorted(char_count, key=char_count.get, reverse=True)

        result = ''
        for char in sorted_chars:
            result += char * char_count[char]
        return result
