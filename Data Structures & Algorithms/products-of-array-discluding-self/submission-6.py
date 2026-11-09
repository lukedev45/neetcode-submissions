class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref_prod = [0] * len(nums)
        suff_prod = [0] * len(nums)
        result = [0] * len(nums)

        pref[0] = suff[len(nums) - 1] = 1

        for idx in range(1, len(nums)):
            pref[i] = nums[i - 1] * pref[i - 1]

        for idx in range(len(nums) - 2, 0):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        for idx in range(len(nums)):
            result[i] = pref[i] * suff[i]

        return result
