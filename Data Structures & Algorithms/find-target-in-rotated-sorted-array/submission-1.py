class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)-1
        low = 0
        high = n

        while low <= high:
            guess =(low +high)//2
            
            if nums[guess] == target:
                return guess

            elif nums[low] <= nums[guess]:
                if nums[low] <= target < nums[guess]:
                    high =guess-1

                else:
                    low = guess + 1      

        

            else:
                if nums[guess] < target <= nums[high]:
                   low=guess+1
                else:
                   high =guess-1                  


              

        return -1          
