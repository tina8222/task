class Treenode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution():
    def isbalanced(self,root):
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
        
            if abs(left - right) > 1:
                return -1
            return 1 + max(left,right)
        
        
        return height(root) != -1
    
    root = Treenode(1,Treenode(2,Treenode(4),Treenode(5)),Treenode(3))
    sol = solution()
    
    print(sol.isbalanced(root))