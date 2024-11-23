#Minimize the Heights II

class Solution {
  public:
    int getMinDiff(vector<int> &arr, int k) {
        // code here
        int n = arr.size();
        if (n == 1) return 0;
        sort(arr.begin(), arr.end());

        int min_diff = arr[n - 1] - arr[0];

        for (int i = 0; i < n-1; i++) {
            int new_min = min(arr[0] + k, arr[i+1] - k);
            int new_max = max(arr[n - 1] - k, arr[i] + k);
            if(new_min<0) continue;

            min_diff = min(min_diff, new_max - new_min);
        }

        return min_diff;
    }
};
