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
//There are two different methods
//Method 1:  using the recursive method, repeat calling itself
class Solution {
public:
    void inorder(TreeNode* root, std::vector<int>& result)
    {
        //This is our base case
        if(!root) //similar as root == NULL
        {
            return;
        }
        inorder(root->left, result);
        result.push_back(root->val);
        inorder(root->right, result);
    }

    vector<int> inorderTraversal(TreeNode* root) {

        std::vector<int> result;
        inorder(root, result);
        return result;
    }
};

/*
//Method 2: using the iteration method, stack -> LIFO to push and pop the values
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> s;
        TreeNode *current = root;

       while (current || !s.empty()) 
       {
            while (current)
            {
                s.push(current);
                current = current->left;
            }

            current = s.top(); //access the element without remove it
            s.pop(); // remove the element
            result.push_back(current->val);

            current = current->right;
        }
        return result;
    }
};






*/