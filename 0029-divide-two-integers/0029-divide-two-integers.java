class Solution {
    public int divide(int dividend, int divisor) {
        // Handle 32-bit overflow edge case
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        // Determine result sign
        boolean negative = (dividend < 0) ^ (divisor < 0);

        // Convert to 64-bit long absolute values to prevent overflow
        long a = Math.abs((long) dividend);
        long b = Math.abs((long) divisor);
        int quotient = 0;

        while (a >= b) {
            long tempB = b;
            int multiple = 1;

            while (a >= (tempB << 1)) {
                tempB <<= 1;
                multiple <<= 1;
            }

            a -= tempB;
            quotient += multiple;
        }

        return negative ? -quotient : quotient;
    }
}