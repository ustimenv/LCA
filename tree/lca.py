from tree import Node

class LCA:
    def __init__(self):
        self.N = Node()

    def findLCA(self, tree, A, B):
        """
    
        :param tree: Tree or subtree we are to search
        :param A:   A node in the tree
        :param B:   Another node in the tree
        """

        if A.data == tree.val or B.val == tree.val:
            return tree

        leftTree = self.findLCA(tree.left, A, B)
        rightTree = self.findLCA(tree.right, A, B)

        if leftTree is None and rightTree is None:
            return None

        if leftTree is not None and rightTree is not None:
            return tree

        if leftTree is None:
            return rightTree
        else:
            return leftTree


if __name__  == "__main__":
    pass