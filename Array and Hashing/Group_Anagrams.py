def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a hashmap with defaultDict(list) for storing the result values. This dict will have the letter count as keys and the matching anagrams as values.
        res = collections.defaultdict(list)

        for char in strs:
            count = [0] * 26 #to count the letters in the character. This data will be used as the key in our res dict. Multiplied by 26 because a,b,c,..., z  = 26

            for letter in char:
                count[ord(letter) - ord("a")] += 1 #adds the value in that particular index thus counting the number of letters
            res[tuple(count)].append(char) # stores the values of the char that has same count of letters. The tuple is used because list doesn't work as key in hashmap

        return res.values() # returning only values 
      
      
      #time_complexity = O(m.n) where m is the maximum length of a char. and n is the length of strs
