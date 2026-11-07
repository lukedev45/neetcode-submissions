class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for k, n in enumerate(nums):
            diff = target - nums[n]
            if diff in hash_map:
                return [hash_map[diff, k]]
            hash_map[n] = i