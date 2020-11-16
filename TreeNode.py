class TreeNode:
    """
    Binary Search Tree Node class
    """
    def __init__(self, value: object, pos: int) -> None:
        """
        Init new Binary Search Tree
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree
        self.pos = pos