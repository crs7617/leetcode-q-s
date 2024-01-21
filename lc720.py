class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        word_set, ans = set(['']), ''

        for word in words:
            if word[:-1] in word_set:
                if len(word) > len(ans):
                    ans=word
                    word_set.add(word)
        return ans
