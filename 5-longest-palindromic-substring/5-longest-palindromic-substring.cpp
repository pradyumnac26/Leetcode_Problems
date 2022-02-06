class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        string x = "";
        bool table[n][n];
        memset(table,0,sizeof(table));
        int maxLength = 1;
        for(int i=0;i<n;i++)
        {
            table[i][i] = true;
        }
        int start = 0;
        for(int i=0;i<n-1;i++)
        {
            if(s[i] == s[i+1])
            {
                maxLength = 2;
                start = i;
                table[i][i+1] = true;
            }
        }
        for(int k=3;k<=n ;k++)
        {
            for(int i=0;i<n-k+1;i++)
            {
                int j = i+k-1;
                if(s[i]== s[j]  && table[i+1][j-1] == true)
                {
                    table[i][j] = true;
                    if(k>maxLength)
                    {
                        maxLength = k;
                        start = i;  
                    }
                }
                
            }
        }
        for(int i = start ; i<= start+maxLength -1 ;i++)
        {
            x = x+s[i];
        }
        return x;
        
    }
};