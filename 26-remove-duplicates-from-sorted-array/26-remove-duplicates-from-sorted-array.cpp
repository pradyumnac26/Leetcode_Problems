class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set<int> s;
        int i;
        for(i=0;i<nums.size();i++)
        {
            s.insert(nums[i]);
        }
        //bcuz they told to modify the same array 
        nums.assign(s.begin(),s.end());
        return nums.size();
    }
};