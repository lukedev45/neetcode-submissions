class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref_prod = [0] * len(nums)
        suff_prod = [0] * len(nums)
        result = [0] * len(nums)

        pref_prod[0] = suff_prod[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            pref_prod[i] = nums[i - 1] * pref_prod[i - 1]

        for i in range(len(nums) - 2, 0):
            suff_prod[i] = nums[i + 1] * suff_prod[i + 1]
        
        for i in range(len(nums)):
            result[i] = pref[i] * suff[i]

        return result
