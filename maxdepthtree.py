class Treenode:
    def __init__(self, val=0 ,left=None,right=None):  
        self.val = val
        self.left = left
        self.right = right 
    
    
class solution:
    def maxdepth(self,root):
        if not root:
            return 0
        left_depth = self.maxdepth(root.left)
        right_depth = self.maxdepth(root.right)
        
        return 1 + max(left_depth,right_depth)
    
    
root = Treenode(3,
                Treenode(9),
                Treenode(20,Treenode(15),Treenode(7)))

sol = solution()
print(sol.maxdepth(root))

        