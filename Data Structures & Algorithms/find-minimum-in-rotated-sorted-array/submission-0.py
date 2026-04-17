class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low =0
        high =n-1

        while low < high:
            guess =(low +high)//2

            if  nums[guess] > nums[high]:
                low =guess+1    

            else:
                 high = guess

        return nums[low]    

          
