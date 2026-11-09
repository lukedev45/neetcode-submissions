class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        
        for string in strs:
            counter = [0] * 26
            for c in string:
                counter[ord(c) - ord('a')] += 1
            hash_map[tuple(counter)].append(string)
        
        return list(hash_map.values())