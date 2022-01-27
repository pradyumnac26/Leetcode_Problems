class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> b;
        int n = nums.size();
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(nums[i]+nums[j] == target)
                {
                    b.push_back(i);
                    b.push_back(j);
                    
                }
            }
        }
        return b;
        
        
    }
};