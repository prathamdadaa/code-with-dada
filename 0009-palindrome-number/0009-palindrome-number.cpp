class Solution {
public:
    bool isPalindrome(int x) {
        // Special cases:
        // Negative numbers are not palindromes.
        // Numbers ending in 0 (except 0 itself) are not palindromes.
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int reversed_num = 0;
        while (x > reversed_num) {
            reversed_num = reversed_num * 10 + x % 10;
            x /= 10;
        }

        // For even digits: x == reversed_num
        // For odd digits: x == reversed_num / 10
        return x == reversed_num || x == reversed_num / 10;
    }
};