from my_queue import Queue 
from TreeNode import TreeNode

class BST:
    def __init__(self, start_tree = None) -> None:
        """
        Init new Binary Search Tree
        """
        self.root = None
        self.staticPos = 0
        
        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)
        

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, current, values):
        """
        Helper method for __str__. Does in-order tree traversal
        """
        # base case
        if current is None:
            return
        # recursive case for left subtree
        if current.left:
            self._str_helper(current.left, values)
        # store value of current node
        values.append(str(current.value))
        # recursive case for right subtree
        if current.right:
            self._str_helper(current.right, values)

    def add(self, value: object) -> None:
        """
        This method adds a new value to the tree, maintaining the BST property.
        :param value: Any object passed to the tree
        :return: The tree is returned
        """
        if self.contains(value) != None:
            return
        node = TreeNode(value, self.staticPos)
        self.staticPos += 1
        x = self.root
        y = None

        while x is not None:
            y = x
            if value < x.value:
                x = x.left
            else:
                x = x.right

        if y is None:
            y = node
            self.root = y

        elif value < y.value:
            y.left = node

        else:
            y.right = node

    def contains_helper(self, root, value):
        if root is None:
            return None
        if root.value == value:
            return root.pos
        elif value < root.value:
            return self.contains_helper(root.left, value)
        else:
            return self.contains_helper(root.right, value)

    def contains(self, value: object) -> bool:
        """
        This method returns True if the value parameter is in the BinaryTree
        or False if it is not in the tree.
        If the tree is empty, the method returns False.
        """
        return self.contains_helper(self.root, value)

    

    def pre_order_traversal_helper(self, queue, root):
        """
        This is the helper method for the recursive pre-order traversal method
        :param queue:
        :param root:
        :return:
        """
        if root is not None:
            queue.enqueue(root)
            self.pre_order_traversal_helper(queue, root.left)
            self.pre_order_traversal_helper(queue, root.right)

    def pre_order_traversal(self) -> Queue:
        """
        This method performs a recursive pre-order traversal of the tree,
        and returns a my_queue object that contains values of visited nodes,
        in the order they were visited.
        """
        q = Queue()
        self.pre_order_traversal_helper(q, self.root)
        return q

    def in_order_traversal_helper(self, queue, root):
        """
        This method is the helper method for the recursive in-order traversal method
        :param queue:
        :param root:
        :return:
        """
        if root is not None:
            self.in_order_traversal_helper(queue, root.left)
            queue.enqueue(root)
            self.in_order_traversal_helper(queue, root.right)

    def in_order_traversal(self) -> Queue:
        """
        This method performs a recursive in-order traversal of the tree,
        and returns a my_queue object that contains values of visited nodes,
        in the order they were visited.
        :return:
        """
        q = Queue()
        self.in_order_traversal_helper(q, self.root)
        return q

    def post_order_traversal_helper(self, queue, root):
        """
        This method is the helper for the recursive post-order traversal method
        :param queue:
        :param root:
        :return:
        """
        if root is not None:
            self.post_order_traversal_helper(queue, root.left)
            self.post_order_traversal_helper(queue, root.right)
            queue.enqueue(root)

    def post_order_traversal(self) -> Queue:
        """
        This method performs a recursive post-order traversal of the tree,
        and returns a my_queue object that contains values of visited nodes,
        in the order they were visited.
        :return:
        """
        q = Queue()
        self.post_order_traversal_helper(q, self.root)
        return q

    def by_level_traversal_helper(self, queue, root, level):
        if root is not None:
            if level == 0:
                queue.enqueue(root.value)
            else:
                self.by_level_traversal_helper(queue, root.left, level - 1)
                self.by_level_traversal_helper(queue, root.right, level - 1)

    def by_level_traversal(self) -> Queue:
        """
        This method performs by-level traversal of the tree,
        and returns a my_queue object that contains values of visited nodes,
        in the order they were visited.
        """
        height = self.height()
        queue = Queue()
        for i in range(height + 1):
            self.by_level_traversal_helper(queue, self.root, i)
        return queue

    def size_helper(self, root):
        """

        :param root:
        :return:
        """
        count = 1
        if root.left is not None:
            count += self.size_helper(root.left)
        if root.right is not None:
            count += self.size_helper(root.right)
        return count

    def size(self) -> int:
        """
        This method returns the total number of nodes in the tree.
        """
        if self.root is None:
            return 0
        return self.size_helper(self.root)

    def height_helper(self, root):
        if root is None:
            return -1
        left = self.height_helper(root.left)
        right = self.height_helper(root.right)
        return 1 + max(left, right)

    def height(self) -> int:
        """
        This method returns the height of the binary tree.
        An empty tree has a height of -1.
        A tree consisting of a single root node returns a height of 0.
        """
        if self.root is None:
            return -1
        return self.height_helper(self.root)


if __name__ == '__main__':
    """ add() example #1 """
    print("\nadd() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add('bravo')
    tree.add('oscar')
    tree.add('sierra')
    print(tree)
    tree.add('charlie')
    tree.add('foxtrott')
    print(tree)
    tree.add('x-ray')
    print(tree)
    q = tree.in_order_traversal()
    while not q.is_empty():
        node = q.dequeue()
        print(node.value, node.pos)

    """ add() example 2 """
    print("\nadd() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\ncontains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(10))
    print(tree.contains(-3))



    
