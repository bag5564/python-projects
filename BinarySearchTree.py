#Lab #6
#Due Date: 03/22/2020, 11:59PM
########################################
#
# Name: Benjamin Gutierrez
# Collaboration Statement:
#
########################################

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return ("Node({})".format(self.value))

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(x.root,9)
        >>> x.getMin
        9
        >>> x.insert(x.root,11)
        >>> x.getMin
        9
        >>> x.insert(x.root,4)
        >>> x.getMin
        4
        >>> x.insert(x.root,2)
        >>> x.insert(x.root,5)
        >>> x.insert(x.root,10)
        >>> x.insert(x.root,9.5)
        >>> x.insert(x.root,7)
        >>> x.getMin
        2
        >>> x.getHeight(x.root)
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.isEmpty()
        False
        >>> x.getHeight(x.root.right.left.left)
        0
    '''
    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if(node==None):
            self.root = Node(value)
        else:
            if(value<node.value):
                if(node.left==None):
                    node.left = Node(value)
                else:
                    self.insert(node.left, value)
            else:
                if(node.right==None):
                    node.right = Node(value)
                else:
                    self.insert(node.right, value)


    def isEmpty(self):
        return self.root == None



    @property
    def getMin(self):
        if self.isEmpty():
          return None
        current = self.root
        # Loop down through the tree to find the leftmost node
        while (current.left != None):
          current = current.left;
        return current.value


    def getHeight(self, node):
        if node == None:
          return None
        # if the node is a leaf
        if node.left == None and node.right == None:
          return 0
        # there is only a right branch under this node
        elif node.left == None:
          return 1 + self.getHeight(node.right)
        # there is only a left branch under this node
        elif node.right == None:
          return 1 + self.getHeight(node.left)
        else:
          return 1 + max(self.getHeight(node.right), self.getHeight(node.left))



