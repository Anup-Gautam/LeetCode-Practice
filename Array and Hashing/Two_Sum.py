class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a dict to store the values with their index
        idxDict = {}
        for idx, num in enumerate(nums): # enumerate() is used to take idx and values
            value = target - num # since num + value should be qual to target, and check whether value is in the dict or not
            if value not in idxDict:
                idxDict[num] = idx # adding the value and index in the dictionary
            else:
                return [idx, idxDict[value]] # returns the current index and the value index that results to target
    

    # space complexity = O(n)
    #time complexity = O(n)
