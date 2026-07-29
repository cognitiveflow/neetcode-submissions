class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett=set()
        for i in range(len(nums)):
            sett.add(nums[i])
        
        if len(nums) == len(sett):
            return False
        else:
            return True
