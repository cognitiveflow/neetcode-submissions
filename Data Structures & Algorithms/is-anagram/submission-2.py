class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted (t) #sorted converts everything into a list with 
        #order and count
            