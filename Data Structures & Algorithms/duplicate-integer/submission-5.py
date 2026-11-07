class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if set(nums) != nums:
            return True
        return False