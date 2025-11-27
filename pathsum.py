
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def PathSum(self, root, targetSum):
        
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        
        remaining = targetSum - root.val
        
        return (self.PathSum(root.left, remaining) or
                self.PathSum(root.right, remaining))



node7 = TreeNode(7)
node2 = TreeNode(2)
node11 = TreeNode(11, node7, node2)

node13 = TreeNode(13)
node1 = TreeNode(1)
node4_right = TreeNode(4, None, node1)

node4_left = TreeNode(4, node11)
node8 = TreeNode(8, node13, node4_right)

root = TreeNode(5, node4_left, node8)


sol = Solution()
targetSum = 22
result = sol.PathSum(root, targetSum)

print("Target Sum:", targetSum)
print("Path exists?", result)