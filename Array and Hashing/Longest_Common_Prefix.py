class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for idx in range(len(strs[0])): # checking the first word
            for char in strs: # checking each character for the common prefix
                if idx == len(char) or char[idx] != strs[0][idx]: # if idx == len(char) for it to end in shortest char 
                    return res
            res += strs[0][idx] #adding the char
        return res
