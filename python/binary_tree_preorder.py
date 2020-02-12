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
        rArray = []

        
        if root is None:
            return rArray

        # root push to stack
        stack.append(root)
        print(len(stack))
        
        while (len(stack) > 0):
            node = stack.pop()
            rArray.append(node.val)
            
            if node.right is not None:
                stack.append(node.right)
                
            if node.left is not None:
                stack.append(node.left)
                
        return rArray
        
    def preorderRecrusive(self, root):
        rArray = []

        if root is None:
            return rArray
        else:
            rArray.append(root.val)
            if root.left is not None:
                rArray += self.preorderRecrusive(root.left)
            if root.right is not None:
                rArray += self.preorderRecrusive(root.right)

        return rArray

if __name__ == "__main__":
    #root = TreeNode(1)
    #root.left = None
    #root.right = TreeNode(2)
    #root.right.left = TreeNode(3)

    root = TreeNode(1)
    root.left =  TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    print(Solution().preorderTraversal(root))

    print(Solution().preorderRecrusive(root))
    