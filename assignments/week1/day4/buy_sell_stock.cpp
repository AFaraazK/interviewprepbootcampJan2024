class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int curr_profit = 0;
        int l = 0;
        int r = 1;

        while ((l < r) && (r < prices.size())){
            if(prices[l] < prices[r]){
                curr_profit = prices[r] - prices[l];
                max_profit = max(curr_profit, max_profit);
            }
            else{
                l = r;
            }
            r++;
        }
        return max_profit;
    }
};