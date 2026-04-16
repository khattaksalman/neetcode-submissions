class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
              
        first = 0
        last = 1

        while first < last:
            if nums[first] == nums[last]:
                return nums[first]

            last+=1
            first+=1

        return None        



              