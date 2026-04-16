class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [c.lower() for c in s if c.isalnum()]
        forward = 0
        backward = len(a)-1

        while forward < backward:
            if a[forward] != a[backward]:
                return False
                break
            forward += 1
            backward -= 1
    
        return True  