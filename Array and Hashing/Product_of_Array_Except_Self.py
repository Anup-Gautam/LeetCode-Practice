class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
           # output List
            res = [1] * len(nums)
            # determining a multiplier prefix
            prefix = 1
            for idx in range(len(nums)):
                res[idx] = prefix 
                prefix *= nums[idx]# multiplies and stores the prefix in output List
            #determining a multiplier postfix
            postfix = 1
            for idx in range(len(nums)-1,-1,-1):
                res[idx] *= postfix # not equating because it will overwrite res value
                postfix *= nums[idx] 
            
            return res

            
            
            
            #time complexity = O(n)
            #space complexity = O(1)
