import SLLQueue
from Interfaces import Tree


class BinaryTree(Tree):
    class Node:
        def __init__(self, key: object = None, val: object = None):
            self.parent = self.left = self.right = None
            self.k = key
            self.v = val

        def set_key(self, x):
            self.k = x

        def set_val(self, v):
            self.v = v

        def insert_left(self, u):
            self.left = u
            self.left.parent = self
            return self.left

        def insert_right(self, u):
            self.right = u
            self.right.parent = self
            return self.right

        def __str__(self):
            return f"({self.k}, {self.v})"

    def __init__(self):
        """
        BinaryTree constructor; initializes an empty binary tree
        """
        self.r = None

    def depth(self, u: Node) -> int:
        """
        returns the path length between the root and the given node.
        :param u: Node type; the node of interest
        :return: int type; the depth of the given node
        """

        if u == None:
            return -1

        curNode = u
        depthCounter = 0

        while (curNode != self.r):
            
            curNode = curNode.parent
            depthCounter += 1


        return depthCounter

    def height(self) -> int:
        """
        returns the height of this binary tree, i.e. the length of the
        longest path that exists from the root to a leaf node.
        :return: int type;
        """
        return self._height(self.r)

    def _height(self, u: Node) -> int:
        """
        helper method; returns the height of the subtree rooted at the given node.
        :param u: Node type; the node of interest
        :return: int type;
        """

        if u == None:
            return -1
        
        return 1 + max(self._height(u.left), self._height(u.right))


        

    def size(self) -> int:
        return self._size(self.r)

    def _size(self, u: Node) -> int:
        """
        helper method for size(); returns the size of the subtree
        rooted at the given node.
        :param u: Node type; the root of the subtree
        """

        if u == None:
            return 0
        else:
            return 1 + self._size(u.left) + self._size(u.right)

        

    def bf_order(self):
        """
        returns a list of nodes as they are traversed in breadth-first order
        :return: list type; a list of Node objects
        """
        
        nodes_list = []
        queue = SLLQueue.SLLQueue()

        if self.r != None:
            queue.add(self.r)
        
        while queue.size() > 0:
            u = queue.remove()
            nodes_list.append(u)
            if u.left != None:
                queue.add(u.left)
            if u.right != None:
                queue.add(u.right)


        return nodes_list

    def in_order(self) -> list:
        """
        returns a list of all nodes in the tree as they are
        traversed using in-order traversal
        :return: list type; a list of Node objects
        """
        return self._in_order(self.r)

    def _in_order(self, u: Node) -> list:
        """
        helper method for in_order(); returns the list nodes
        in the subtree rooted at the given node, as they are traversed
        using in-order traversal
        :param u: Node type; the root of the subtree
        """

        nodes_list = []

        if u.left != None:

            nodes_list.extend(self._in_order(u.left))
        
        nodes_list.append(u)
        
        if u.right != None:
            nodes_list.extend(self._in_order(u.right))

        return nodes_list

    def post_order(self) -> list:
        """
        returns a list of all nodes in the tree as they are
        traversed using post-order traversal
        :return: list type; a list of Node objects
        """
        return self._post_order(self.r)

    def _post_order(self, u: Node):
        """
        helper method for post_order(); returns the list nodes
        in the subtree rooted at the given node, as they are traversed
        using post-order traversal
        :param u: Node type; the root of the subtree
        """

        nodes_list = []

        if u.left != None:
            nodes_list.extend(self._post_order(u.left))
        
        if u.right != None:
            nodes_list.extend(self._post_order(u.right))

        nodes_list.append(u)

        return nodes_list



    def pre_order(self) -> list:
        """
        returns a list of all nodes in the tree as they are
        traversed using pre-order traversal
        :return: list type; a list of Node objects
        """
        return self._pre_order(self.r)

    def _pre_order(self, u: Node):
        """
        helper method for pre_order(); returns the list nodes
        in the subtree rooted at the given node, as they are traversed
        using pre-order traversal
        :param u: Node type; the root of the subtree
        """

        nodes_list = []

        nodes_list.append(u)

        if u.left != None:
            nodes_list.extend(self._pre_order(u.left))
        
        if u.right != None:
            nodes_list.extend(self._pre_order(u.right))

        

        return nodes_list



    def __str__(self):
        """
        returns a string of the nodes as they are traversed using BF order
        :return: str type;
        """
        nodes = self.bf_order()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)



