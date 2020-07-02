// https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/

#include<iostream>
#include<string>
using namespace std;

class Solution {
public:
    string replaceSpace(string s) {
        if (s.length() == 0)
            return s;
        string res;
        for (int i = 0; i < s.length(); i++) 
        {
            if (s[i] == ' ')
                res += "%20";
            else
                res += s[i];
        }
        return res;
    }

    string replaceSpace2(string s) {
        if (s.length() == 0)
            return s;
        int cnt = 0;
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] == ' ')
                cnt += 1;
        }
        int j = s.length() + cnt * 2;
        for (int i = s.length(); i >= 0; i--)
        {
            if (s[i] != ' ')
                s[j--] = s[i];
            else
            {
                s[j--] = '0';
                s[j--] = '2';
                s[j--] = '%';
            }
        }
        return s;
    }
};

int main()
{
    Solution s = Solution();
    string a = s.replaceSpace("sf d");
    cout << a;

    return 0;
}