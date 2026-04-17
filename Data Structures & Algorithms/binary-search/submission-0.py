class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high =n-1

        while low <= high:
            guess = (low + high) // 2

            if nums[guess] < target:
                low =guess+1

            elif nums[guess] > target:
                high =guess-1

            else:
                return guess

        return -1                
        