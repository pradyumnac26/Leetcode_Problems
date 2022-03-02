class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> b;
        for(int i=0;i<=n;i++)
        {
            int sum = 0;
            int p = i;
            while(p!=0)
            {
                sum+=p%2;
                p=p/2;
            }
            b.push_back(sum);
        }
        return b;
    }
    
};