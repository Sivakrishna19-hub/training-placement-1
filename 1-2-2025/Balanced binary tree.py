class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def is_balanced(root):
    if not root:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(root.left) and is_balanced(root.right)

# Example Usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)  # Unbalanced case

print("Is the tree balanced?", is_balanced(root))  # Output: False
