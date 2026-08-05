class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        #outer loop: walk each position of the first word
        for i in range(0, len(strs[0])):
            char = strs[0][i] #lock in the first word and walk each position

            #inner loop: check the same position in every other word
            for word in strs[1:]: #from the 2nd word to the end of the list
                if i >= len(word)  or word[i]!= char: 
                    return strs[0][:i] #return the string so far
        #if no mismatch then return the first work
        return strs[0]


