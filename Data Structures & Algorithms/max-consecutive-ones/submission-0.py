class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      
        i = 0
        j = 0
        max_len=0
        while j < len(nums):
            if nums[j] == 0:
                i = j+1

            max_len=max(max_len,j-i+1)
            j+=1
        return max_len    


