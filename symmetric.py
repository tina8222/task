
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]

    for i in range(len(values)):
        if nodes[i] is None:
            continue
        left_i = 2*i + 1
        right_i = 2*i + 2
        if left_i < len(values):
            nodes[i].left = nodes[left_i]
        if right_i < len(values):
            nodes[i].right = nodes[right_i]

    return nodes[0]

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and
                self.isMirror(t1.left, t2.right) and
                self.isMirror(t1.right, t2.left))


tree1 = build_tree([1, 2, 2, 3, 4, 4, 3])  
tree2 = build_tree([1, 2, 2, None, 3, None, 3])  

sol = Solution()
print(sol.isSymmetric(tree1))  # True
print(sol.isSymmetric(tree2))  # False