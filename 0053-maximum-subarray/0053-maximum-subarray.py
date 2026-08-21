class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def find_max_cross_subarray(left: int, mid: int, right: int) -> int:
            # Maximum sum starting from mid and moving left
            left_sum = float('-inf')
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)
            
            # Maximum sum starting from mid + 1 and moving right
            right_sum = float('-inf')
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)
                
            return left_sum + right_sum

        def divide_and_conquer(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            left_max = divide_and_conquer(left, mid)
            right_max = divide_and_conquer(mid + 1, right)
            cross_max = find_max_cross_subarray(left, mid, right)
            
            return max(left_max, right_max, cross_max)

        return divide_and_conquer(0, len(nums) - 1)