class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}


        for i in range(len(s)):
            ch = s[i]

            if ch in hash1:
              hash1[ch] += 1
            else:
               hash1[ch] = 1

        for j in range(len(t)):
            ch = t[j]

            if ch in hash2:
                hash2[ch] += 1

            else:
                 hash2[ch] =1         
        

        if hash1 == hash2:
            return True

        return False    