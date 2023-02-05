class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dictionary to count duplicate
        res = {}

        for num in nums:
            if num not in res:
                res[num] = 1;
            else:
                res[num] += 1

        max_list = [] #our output list
        while len(max_list) < k:
            max_val = max(res, key=res.get) # getting the max key of from the dictionary
            max_list.append(max_val)
            del res[max_val]#removing the max key from the dictionary so that the next max value only remains.
        
        return max_list

      #space_complexity : o(n)
      #time_complexity: o(n)
