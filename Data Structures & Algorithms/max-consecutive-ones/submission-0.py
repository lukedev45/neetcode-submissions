class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tot_count = []
        con_count = 0
        for element in nums:
            if element == 1:
                con_count += 1
            else:
                con_count = 0
            tot_count.append(con_count)
        return max(tot_count)

                