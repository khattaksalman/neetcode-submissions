class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        for i in range(len(word)):
            if i == len(word)-1:
                return len(word[i])
                
        