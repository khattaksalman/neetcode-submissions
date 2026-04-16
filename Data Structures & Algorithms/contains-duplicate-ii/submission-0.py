class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dublicate = set()
        
        for i in range(len(nums)):
            if nums[i] in dublicate:
                return True

            dublicate.add(nums[i])
            
            if len(dublicate) > k:
                dublicate.remove(nums[i-k])


        return False        
        