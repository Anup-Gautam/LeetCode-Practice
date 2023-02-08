class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # create two pointers
        l = 0 
        r = len(numbers) - 1
        #this is an sorted array
        while l <= r:
            if numbers[l] + numbers[r] < target: # becacuse sum will increase as left pointer moves forward
                l += 1
            elif numbers[l] + numbers[r] > target: # because sum will decrease as right pointer moves backward
                r -= 1
            elif numbers[l] + numbers[r] == target:
                return [l + 1, r + 1] 

        #space complexity = o(n)
        #time complexity = o(1)
