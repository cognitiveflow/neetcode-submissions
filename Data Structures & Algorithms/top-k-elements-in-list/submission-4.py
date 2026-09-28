class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        """
        from collections import Counter
        nums.sort()
        count_dict = Counter(nums)#counter has most common. It is a dict subclass
        
        count_list = count_dict.most_common(k) #returns a list of key value pairs
            
            #nums = []
            #for i in range(len(count_list)):
            #    print(count_list[i][0])
            #    nums.append(count_list[i][0])
            #

        return [num for num, count in count_list]
        """
        frequencies = {} #to track freq.
        #count each number's freq
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            elif num in frequencies:
                frequencies[num] += 1
        #print (frequencies)

        #sort the frequencies dict based on the frequencies, highest first (desc)

        frequencies = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
        #print (frequencies)
        
        #extract the freq. for a list of tuples & return a list
        result = [num[0] for num in frequencies[:k]]
        print (result)
        return result
        
                

        
        