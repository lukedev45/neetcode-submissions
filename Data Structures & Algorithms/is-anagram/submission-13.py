class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}

        for letter in s:
            hash_map_s[letter] = 1 + hash_map_s.get(letter, 0)
        for letter in t:
            hash_map_t[letter] = 1 + hash_map_t.get(letter, 0)
        
        return hash_map_s.items() == hash_map_t.items()
