class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in nums:
            y = target - x
            if y in nums and y != x:
                return [nums.index(x), nums.index(y)]
                break
        