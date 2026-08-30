class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_dict = {}
        for word in strs:
            key = "".join(sorted(word)) #sorted creates a sorted list of characters from the strings. "".joins enjoins them without placing a space in between.
        #if key not in groups_dict:
        #    groups_dict[key] = [] # manually create the empty bucket
            groups_dict.setdefault(key, []).append(word)
        return list(groups_dict.values())

        