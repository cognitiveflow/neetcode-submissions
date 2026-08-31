class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #for num in nums[:]:
        #    if num == val:
        #        nums.remove(val)
                #print(nums)
        nums[:] = [n for n in nums if n != val]
        return len(nums)

        