class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = set(nums)
        for idx in range(len(nums)):
            difference = target - nums[idx]
            if difference in hash_map and hash_map[diff] != idx:
                indices.append(nums.index(difference))
        return indices