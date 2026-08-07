class Solution:

  def firstMissingPositive(self, nums: list[int]) -> int:
    n = len(nums)

    # Step 1: Place each number in its correct slot (nums[i] at index nums[i] - 1)
    for i in range(n):
      while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        correct_idx = nums[i] - 1
        nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

    # Step 2: Find the first index where value does not equal index + 1
    for i in range(n):
      if nums[i] != i + 1:
        return i + 1

    # Step 3: If all numbers 1..n are present, return n + 1
    return n + 1