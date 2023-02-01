class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the length is not same they cannot be anagrams
        if len(s) != len(t):
            return False
        #create a dictionary to count char in each string
        countS = {}
        countT = {}
        for idx in range(len(s)):
            countS[s[idx]] = 1 + countS.get(s[idx],0) #creates a counter for each letter
            countT[t[idx]] = 1 + countT.get(t[idx],0)
        if countS != countT: # checking if dictionary has same keys and values
                return False
        return True

    #space Complexity : o(n)
    #time Complexity : o(n)
