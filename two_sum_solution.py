from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        #iterate through the array
        for i, num in enumerate(nums):
            #we calculate the complement value
            complement = target - num
            #check if the complement is found ithe dict
            if complement in num_indices:
                #return the complement and its index
                return (num_indices[compolement], i)
            #we add it to the existing dict
            num_indices[num] = i
        return []
