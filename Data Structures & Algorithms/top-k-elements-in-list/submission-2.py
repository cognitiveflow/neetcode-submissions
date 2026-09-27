class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        nums.sort()
        count_dict = Counter(nums)#counter has most common. It is a dict subclass
        
        count_list = count_dict.most_common(k) #returns a list of key value pairs
        
        nums = []
        for i in range(len(count_list)):
            print(count_list[i][0])
            nums.append(count_list[i][0])
        
        
        return nums
        