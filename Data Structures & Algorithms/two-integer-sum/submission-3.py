class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = []
        for x in range(len(nums)):
            difference = target - nums[x]
            if difference in nums: 
                hash_map.append(x)
        return hash_map
        