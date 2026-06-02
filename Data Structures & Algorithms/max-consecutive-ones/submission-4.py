class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        top_count = []
        curr_count = 0
        
        for num in nums:
            if num == 1:
                curr_count += 1
            else:
                top_count.append(curr_count)
                curr_count = 0

        top_count.append(curr_count)
        return max(top_count)