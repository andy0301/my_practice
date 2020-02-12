#!/usr/local/bin/python3

# Binary tree preorder traversal
# Root ->  Left -> Right

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def preorderTraversal(self, root):
        stack = []
        rAarray = []

        
        if root is None:
            return rAarray

        # root push to stack
        stack.append(root)
        print(len(stack))
        
        while (len(stack) > 0):
            node = stack.pop()
            rAarray.append(node.val)
            
            if node.right is not None:
                stack.append(node.right)
                
            if node.left is not None:
                stack.append(node.left)
                
        return rAarray
        

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(Solution().preorderTraversal(root))
    