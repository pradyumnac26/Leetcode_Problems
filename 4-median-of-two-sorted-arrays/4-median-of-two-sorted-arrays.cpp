class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double x;
        nums1.insert(nums1.end(),nums2.begin(),nums2.end());
        sort(nums1.begin(),nums1.end());
        for(int i=0;i<nums1.size();i++)
        {
        cout<<nums1[i];
        }
        int n = nums1.size();
        if(n%2 == 0)
        {
            return (float(nums1[n/2]) + float(nums1[n/2 - 1]))/2;
        }
        else 
        {
            return nums1[n/2] ;
        }
        
        
        
    }
};