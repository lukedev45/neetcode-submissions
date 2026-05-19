class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        total = 0

        for num in nums:
            if num == 1:
                curr += 1
            else:
                total = max(total, curr)
                curr = 0 
        return max(total,curr)