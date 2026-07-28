class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        if len(nums) < 1 or len(nums) > 1000:
            return
        else:
            #ans = []
            ans = nums+nums
            return ans
        


        