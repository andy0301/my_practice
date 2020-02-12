#!/usr/local/bin/python

# Binary tree inorder traversal
# Left -> Root -> Right
"""
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        stack = []
        rArray = []
        
        if root is None:
            return rArray
        
        current = root
        while current is not None:
            stack.append(current)
            current = current.left
        
        while (len(stack) > 0 and current is None):
            node = stack.pop()
            rArray.append(node.val)
            
            current = node.right
            while current is not None:
                stack.append(current)
                current = current.left
                        
        return rArray

    def inorderRecrusive(self, root: TreeNode):
        rArray = []

        if root is None:
            return rArray
        else:
            if root.left is not None:
                rArray = self.inorderRecrusive(root.left)
            rArray.append(root.val)
            if root.right is not None:
                rArray += self.inorderRecrusive(root.right)

        return rArray

        
if __name__ == "__main__":
    root = TreeNode(1)
    root.left =  TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    print(Solution().inorderTraversal(root))

    print(Solution().inorderRecrusive(root))