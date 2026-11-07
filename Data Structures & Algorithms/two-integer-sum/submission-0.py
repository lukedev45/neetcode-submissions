class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in nums:
            y = target - x
            if y in nums:
                return [nums.index(x), nums.index(y)]
                break
        