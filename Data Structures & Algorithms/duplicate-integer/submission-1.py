class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            seen.add(nums[i])
        
        if len(nums) == len(seen):
            return False
        else:
            return True
