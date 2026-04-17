class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap ={}

        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            
            else:
                hashmap[i]=1

        max_value = max(hashmap.values())

        for k, v in hashmap.items():
           if v == max_value:
              return k      
        