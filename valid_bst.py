##https://leetcode.com/problems/validate-binary-search-tree/
class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def valid_bst(self, root: TreeNode, minimo = float('-inf'), maximo = float('inf')) -> bool:
    if not root:
      return True
    if root.val <= minimo or root.val >= maximo:
      return False
    return self.valid_bst(root.left, minimo, root.val) and self.valid_bst(root.right, root.val, maximo)
