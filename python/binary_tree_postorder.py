#!/usr/local/bin/python3

# Left -> Right -> Root

class TreeNode():
    def __init__ (self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def postorderTraversal(self, root):
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

            if node.right is not None:
                stack.append(node)
                current = node.right
                while current is not None:
                    stack.append(current)
                    current = current.right

            rArray.append(node.val)

        return rArray 


    def postorderRecrusive(self, root):
        rArray = []
        if root is None:
            return rArray
        else:
            if root.left is not None:
                rArray = self.postorderRecrusive(root.left)
            if root.right is not None:
                rArray += self.postorderRecrusive(root.right)
            rArray.append(root.val)

        return rArray


if __name__ == "__main__":
    root = TreeNode(1)
    root.left =  TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    print(Solution().postorderRecrusive(root))

    print(Solution().postorderTraversal(root))