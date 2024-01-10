/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int ans;
    int amountOfTime(TreeNode* root, int start) {
        dfs(root,start);
        return ans;
        
    }
    int dfs(TreeNode* node, int start){
        if(node==NULL ) return 0;

        int ld=dfs(node->left,start);
        int rd=dfs(node->right,start);

        if(node->val  == start){
            ans=std::max(ld,rd);
            return -1;
        }
        else if(ld>=0 && rd>=0){
            return std::max(ld,rd)+1;
        }
        ans=std::max(ans,std::abs(ld-rd));
        return std::min(ld,rd)-1;
    }
};
