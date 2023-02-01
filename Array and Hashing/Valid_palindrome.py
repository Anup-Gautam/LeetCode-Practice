class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer method
        l = 0
        r = len(s) - 1
        while l < r: # will work until the pointers meet or pass each other
            while l < r and not self.alphaNum(s[l]): # checking alphanumeric on the left side
                l = l + 1
            while l < r and not self.alphaNum(s[r]): # checking alphanumeric on the right side
                r = r - 1

        # we do l<r  while checking alphaNumeric so that the order of the index when they are at the middle or the chance to pass each other doesn't create an error
            print ([s[l],s[r]]) # checking to see the two pointers
            if s[l].lower() != s[r].lower():
                return False # if even one pointer doesn't match, they can't be a palindrome
            l += 1
            r -= 1
        return True
        
    #creating a helper function to seperate alphaNumeric characters to spaces and punctuations
    def alphaNum(self, char):
        return (ord("A") <= ord(char) <= ord("Z") or
        ord("a") <= ord(char) <= ord("z") or
        ord("0") <= ord(char) <= ord("9")) # ord() function is used to calculate the ASCII value of the given character
