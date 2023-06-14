# Url: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
MAX_SIZE = 100000

def inorder(root, values):
    if root is None:
        return
    inorder(root.left, values)
    values.append(root.val)
    inorder(root.right, values)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return MAX_SIZE
        
        values = []
        
        inorder(root, values)
        
        n = len(values)
        minDiff = sys.maxsize
        
        for i in range(1, n):
            diff = values[i] - values[i-1]
            if diff < minDiff:
                minDiff = diff
        
        return minDiff