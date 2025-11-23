
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]

    root = kids.pop() 

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))



tree1 = build_tree([1, 2, 3]) 
tree2 = build_tree([1, 2, 3]) 
tree3 = build_tree([1, 2, None])

sol = Solution()

print(sol.isSameTree(tree1, tree2))  # True
print(sol.isSameTree(tree1, tree3))  # False