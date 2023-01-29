class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a Dictonary to count items
        countDict = {}
        for char in nums:
            if char not in countDict:
                countDict[char] = 1
            else:
                return True # since the char is already in the Dictonary, it denotes that duplicate is present
        return False
    
    #Time Complexity = o(n)
    #Space Complexity = o(n)
    
   #in order to do it space complexity o(1), we can use sort but it will change the time complexity to o(n^2)
