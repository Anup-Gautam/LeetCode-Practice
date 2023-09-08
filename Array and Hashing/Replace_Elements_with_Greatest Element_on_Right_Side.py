class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for idx in range(len(arr)-1,-1,-1):
            new_max = max(max_val,arr[idx])#(checking the max val from right Side)
            arr[idx] = max_val #why max_val and not new_max??   
            max_val = new_max
        return arr
