class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j= 0
        new_str = ""
        while i < len(s) and j < len(t):
            if s[i] == t[j]: # waits until a value matches
                new_str += s[i]
                i += 1
            j+= 1
        
        return s == new_str

