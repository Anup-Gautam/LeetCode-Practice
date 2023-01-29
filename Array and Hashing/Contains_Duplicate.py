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
