class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for idx in range(len(nums)):
            y = target - nums[idx]
            if y in hash_map:
                return [hash_map[number], hash_map[y]]
            else:
                hash_map[nums[idx]] = idx
