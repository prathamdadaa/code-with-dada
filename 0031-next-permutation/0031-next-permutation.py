class Solution:

  def nextPermutation(self, nums: list[int]) -> None:
    """Modifies nums in-place to the next lexicographical permutation."""
    n = len(nums)
    i = n - 2

    # Step 1: Find the first decreasing element from the right
    while i >= 0 and nums[i] >= nums[i + 1]:
      i -= 1

    # Step 2: If a pivot is found, find the element just larger than nums[i] to swap
    if i >= 0:
      j = n - 1
      while nums[j] <= nums[i]:
        j -= 1
      nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse the sequence from i + 1 to the end
    left, right = i + 1, n - 1
    while left < right:
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
      right -= 1