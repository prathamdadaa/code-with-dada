class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (n <= 1 || k == 0) return 0;

        // If k is large enough, treat as unlimited transactions
        if (k >= n / 2) {
            int maxProfit = 0;
            for (int i = 1; i < n; i++) {
                if (prices[i] > prices[i - 1]) {
                    maxProfit += prices[i] - prices[i - 1];
                }
            }
            return maxProfit;
        }

        // DP arrays for buy and sell states up to k transactions
        int[] buy = new int[k + 1];
        int[] sell = new int[k + 1];

        // Initialize buy states to negative infinity
        for (int j = 0; j <= k; j++) {
            buy[j] = Integer.MIN_VALUE;
        }

        for (int price : prices) {
            for (int j = 1; j <= k; j++) {
                // Max profit when buying stock for the j-th transaction
                buy[j] = Math.max(buy[j], sell[j - 1] - price);
                
                // Max profit when selling stock for the j-th transaction
                sell[j] = Math.max(sell[j], buy[j] + price);
            }
        }

        return sell[k];
    }
}