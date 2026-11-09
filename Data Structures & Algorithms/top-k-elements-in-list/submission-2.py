class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {} # Pairs digit to their count
        freq = [[] for _ in range(len(nums) + 1)] # Buckets that are indexed by their count 

        for n in nums:
            hash_map[n] = 1 + hash_map.get(n, 0)
        
        for k, v in hash_map.items():
            freq[v].append(k)

        result = []
        for idx in range(len(freq) - 1, 0, -1):
            for digit in freq[idx]:
                result.append(digit)
                if len(result) == k:
                    return result
            

        