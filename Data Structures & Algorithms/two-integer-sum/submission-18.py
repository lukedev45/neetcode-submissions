class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for idx in range(len(nums)):
            y = target - nums[idx]
            if y not in hash_map:
                hash_map[nums[idx]] = idx
            else:
                return [hash_map[nums[idx]], idx]
