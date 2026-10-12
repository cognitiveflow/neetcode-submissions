class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        string = ""
        for s in strs: #iterate over the list elements
            string+= str(len(s)) + "#" + s #convert to a string type as needed and add
        #print(string)
        return string
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res, i = [], 0 #initialize res array and i

        while i < len(s):#length of string
            j=i #another variable
            while s[j] != "#": #find the first # delimeter
                j += 1
            length = int(s[i:j]) #j is not included 
            #print(length)
            res.append(s[j+1 : j+1+length])
            #print(res)
            i = j + 1 + length

        return res
