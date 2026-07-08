# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root):
        # Step 1: Extract elements in sorted order using In-Order Traversal
        sorted_nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
        # Step 2: Rebuild a balanced BST from the sorted nodes list
        def build_balanced_tree(left, right):
            if left > right:
                return None
            
            # Pick the middle element to ensure balance
            mid = (left + right) // 2
            current_root = sorted_nodes[mid]
            
            # Recursively build left and right subtrees
            current_root.left = build_balanced_tree(left, mid - 1)
            current_root.right = build_balanced_tree(mid + 1, right)
            
            return current_root
            
        return build_balanced_tree(0, len(sorted_nodes) - 1)