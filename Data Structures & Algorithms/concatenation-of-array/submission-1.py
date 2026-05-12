class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr =[]

        for idx in range(2 * len(nums)):
            if idx <= len(nums) - 1:
                arr.append(nums[idx])
            else:
                arr.append(nums[idx - len(nums)])

        return arr