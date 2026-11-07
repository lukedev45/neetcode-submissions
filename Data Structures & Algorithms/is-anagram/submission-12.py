class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}

        if len(s) != len(t):
            return False
        
        for letter in s:
            if letter not in hash_map_s:
                hash_map_s[letter] = 1
            else:
                hash_map_s[letter] += 1
        for letter in t:
            if letter not in hash_map_t:
                hash_map_t[letter] = 1       
            else:
                hash_map_t[letter] += 1       
        for letter in hash_map_s.keys():
            if (letter in hash_map_t) and (hash_map_s[letter] == hash_map_t[letter]):
                continue
            else:
                return False
        
        return True