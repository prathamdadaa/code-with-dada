class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is the smaller array to keep binary search efficiency high
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.length;
        int n = nums2.length;
        int halfLen = (m + n + 1) / 2;

        int low = 0;
        int high = m;

        while (low <= high) {
            int i = (low + high) / 2; // Partition index in nums1
            int j = halfLen - i;      // Partition index in nums2

            int maxLeft1 = (i == 0) ? Integer.MIN_VALUE : nums1[i - 1];
            int minRight1 = (i == m) ? Integer.MAX_VALUE : nums1[i];

            int maxLeft2 = (j == 0) ? Integer.MIN_VALUE : nums2[j - 1];
            int minRight2 = (j == n) ? Integer.MAX_VALUE : nums2[j];

            // Check if partition is valid
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                // Odd total length -> max of left side
                if ((m + n) % 2 == 1) {
                    return Math.max(maxLeft1, maxLeft2);
                } 
                // Even total length -> average of max of left side and min of right side
                else {
                    return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2.0;
                }
            } else if (maxLeft1 > minRight2) {
                // Too far right in nums1, move left
                high = i - 1;
            } else {
                // Too far left in nums1, move right
                low = i + 1;
            }
        }

        throw new IllegalArgumentException("Input arrays are not sorted.");
    }
}