class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:        
        maxlen=[]
        maxlen.append(max(nums[:k]))
        l=0
        for i in range(k,len(nums)):
            l+=1
            maximum=max(nums[l:i+1])
            maxlen.append(maximum)
            
        return maxlen    
        