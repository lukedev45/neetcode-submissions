class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr =[]
        n = len(nums)

        for idx in range(2 * n):
            if idx <= n - 1:
                arr.append(nums[idx])
            else:
                arr.append(nums[idx - n])

        return arr