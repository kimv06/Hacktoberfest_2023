#include <iostream>

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
};

int main() {
    // Creating nodes for the binary tree
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    // Accessing and printing the values of the binary tree nodes
    std::cout << "Root Node: " << root->data << std::endl;
    std::cout << "Left Child of Root: " << root->left->data << std::endl;
    std::cout << "Right Child of Root: " << root->right->data << std::endl;
    std::cout << "Left Child of 2: " << root->left->left->data << std::endl;
    std::cout << "Right Child of 2: " << root->left->right->data << std::endl;
    return 0;
}
