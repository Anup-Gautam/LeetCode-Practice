class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip() # incase of additional spaces in front and back i.e "    hello   "
        lolw = 0
        for char in range(len(s)-1,-1,-1): #checking last word
            if s[char] == " ":
                break
            else:
                lolw += 1

        return lolw
