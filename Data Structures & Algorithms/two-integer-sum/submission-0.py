class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #dict/hashmap
        for i, n in enumerate(nums):
            if target - n in seen: #e.g. 6 - 2 = 4 in seen already?
                return [ seen[target - n] , i] # return indices of 2 and 4 in an array. seen[key] is how you access the dict
            seen[n] = i #index is stored as the value and value as index.
        return [] #empty array
                
        