class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            result = []

            # The is always a left and right about some index
            left = 1
            right = 1

            left_product_arr = []
            right_product_arr = []

            for idx in range(len(nums)):
                left *= nums[idx]
                right *= nums[-idx]
                left_product_arr.append(left)
                right_product_arr.append(right)

            
            return right_product_arr