from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0

    def add(self, key: object, value: object = None) -> bool:
        """
        adds a new node with given key and value, in the correct position,
        if an item with the given key does not already exist in the tree.
        :return: bool type; True if the key-value pair was added to the tree, False otherwise.
        """

        newNode = BinaryTree.Node(key, value)
        newParent = self._find_last(key)
        return self._add_child(newParent, newNode)

        

    def find(self, key: object) -> object:
        """
        returns the value corresponding to the given key if the key
        exists in the BinarySearchTree, None otherwise
        :param key: object type; the key to search for
        :return: object type or None; the value corresponding to given key if it
        exists; None, otherwise.
        """

        node = self._find_eq(key)

        if node == None:
            return None

        return node.v
        

    def remove(self, key: object):
        """
        removes the node with given key if it exists in this BinarySearchTree.
        :return: object type; the value corresponding to the removed key, if the key was in the tree.
        :raises: ValueError if given key does not exist in the tree
        """

        u = self._find_eq(key)

        if u == None:
            raise ValueError("Error")
        
        tempValue = u.v
        self._remove_node(u)

        return tempValue
    

    def _find_eq(self, key: object) -> BinaryTree.Node:
        """
        helper method to find(key); returns the node in this tree
        that contains the given key, or None otherwise.
        """

        currentNode = self.r

        while currentNode != None:
            if key < currentNode.k:
                currentNode = currentNode.left
            elif key > currentNode.k:
                currentNode = currentNode.right
            else:
                return currentNode
        
        return None


        

    def _find_last(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key, if it exists.
        Otherwise, returns the node that would have been the parent of the node
        with the given key, if it existed
        :param key: object type; the key to look for
        :return: Node type; the node with the given key if it exists, otherwise, the
                node that would be the parent of a node with given key.
        """

        curNode = self.r
        parentNode = None

        while curNode != None:
            parentNode = curNode
            if key < curNode.k:
                curNode = curNode.left
            elif key > curNode.k:
                curNode = curNode.right
            else:
                return curNode

        return parentNode

        

    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        """
        helper method to add(key, val); adds node u as the child of node p,
        assuming node p has at most 1 child, and the invariant will not be violated
        :param p: Node type; the parent node
        :param u: Node type; the child node
        :return: bool type; True if the child node is successfully added, False otherwise.
        """

        if p == None:
            self.r = u
        else:
            if u.k < p.k:
                p.left = u
            elif u.k > p.k:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True


        

    def _splice(self, u: BinaryTree.Node):
        """
        helper method to remove(key); links the parent of given node u to the child
        of node u, assuming u only has one child
        """

        if u.left != None:
            childNode = u.left
        else:
            childNode = u.right
        
        if u == self.r:
            self.r = childNode
            newParent = None
        else:
            newParent = u.parent
            if newParent.left == u:
                newParent.left = childNode
            else:
                newParent.right = childNode
        
        if childNode != None:
            childNode.parent = newParent
        self.n -= 1


        

    def _remove_node(self, u: BinaryTree.Node):
        """
        helper method to remove(key); removes the given node
        """

        if u.left == None or u.right == None:
            self._splice(u)
        else:
            w = u.right
            while w.left != None:
                w = w.left
        
            u.k = w.k
            u.v = w.v
            self._splice(w)


        

    def clear(self):
        """
        empties this BinarySearchTree
        """

        self.r = None
        self.n = 0

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k
            u = self.next_node(u)

    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left is not None:
            w = w.left
        return w

    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w


    def bookstore_helper(self, prefix: str):
        """
        searches for the first instance of a node whose key begins with the given prefix.
        The search is performed beginning at the root by comparing the prefix of length n
        to the first n characters of the string key of the current node. If the current
        node does not contain the prefix, then the search continues by using the binary search
        tree invariant, namely, that the left child of the current node must have a string key that
        comes before the key of current node in alphabetical order, while the right child of the
        current node must have a key that comes after the key of the current node.
        finds and returns the first node encountered in the tree whose key begins with the given prefix,
        If node exists such that its key contains the given prefix, then None is returned.
        :param prefix: str type;
        :return: BinaryTree.Node or None type;
        """
        pass # FIXME: Replace with your implementation


