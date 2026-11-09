class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            result = []

            # The is always a left and right about some index
            product = 1

            for idx in range(len(nums)):
                prefix = nums[:idx]
                suffix = nums[idx + 1:]
                for num in prefix + suffix:
                    product *= num
                
                result.append(product)
                product = 1
                
            return result