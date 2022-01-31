class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxsofar = INT_MIN;
        int maxendinghere = 0;
        for(int i=0;i<nums.size();i++)
        {
            maxendinghere += nums[i];
            if(maxsofar < maxendinghere)
                maxsofar = maxendinghere;
            if(maxendinghere < 0)
            maxendinghere = 0;
            
            
        }
        return maxsofar;
        
        
        
    }
};