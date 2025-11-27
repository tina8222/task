
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


node4 = TreeNode(4)
node2 = TreeNode(2, left=node4)
node3 = TreeNode(3)
root = TreeNode(1, left=node2, right=node3)



sol = Solution()
result = sol.minDepth(root)

print("Minimum Depth =", result)