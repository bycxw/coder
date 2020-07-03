// https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/submissions/

#include <vector>;
using namespace std;
/**
 * Definition for singly-linked list.
 * */
 struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
 
class Solution {
public:
    vector<int> reversePrint(ListNode* head) {
        // iterative
        vector<int> res;
        if (head == nullptr)
            return res;
        ListNode *pNode = head;
        while (pNode != nullptr)
        {
            res.push_back(pNode -> val);
            pNode = pNode -> next;
        }
        int s = res.size();
        int tmp;
        for (int i = 0; i < s / 2; i++)
        {
            tmp = res[i];
            res[i] = res[s - i - 1];
            res[s - i - 1] = tmp;
        }
        return res;
    }

    vector<int> reversePrint2(ListNode* head) {
        // recursive
        vector<int> res;
        if (head == nullptr)
        {
            return res;
        }
        res = reversePrint2(head->next);
        res.push_back(head->val);
        return res;
    }
};
