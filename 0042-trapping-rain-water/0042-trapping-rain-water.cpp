#include <vector>
#include <algorithm>

class Solution {
public:
    int trap(std::vector<int>& height) {
        if (height.empty()) return 0;

        int left = 0, right = height.size() - 1;
        int left_max = height[left], right_max = height[right];
        int total_water = 0;

        while (left < right) {
            if (left_max < right_max) {
                left++;
                left_max = std::max(left_max, height[left]);
                total_water += left_max - height[left];
            } else {
                right--;
                right_max = std::max(right_max, height[right]);
                total_water += right_max - height[right];
            }
        }

        return total_water;
    }
};