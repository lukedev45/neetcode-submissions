class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}

        if len(s) != len(t):
            return False
        
        for letter in s:
            if hash_map_s[letter] == 0:
                hash_map_s[letter] += 1
            else:
                hash_map_s[letter] += 1
        for letter in t:
            if hash_map_t[letter] == None:
                hash_map_t[letter] += 1       
        
        for letter in hash_map_s.keys():
            if hash_map_s[letter] == hash_map_t[letter]:
                continue
            else:
                return False
        
        return True