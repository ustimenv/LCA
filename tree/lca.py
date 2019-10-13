from treeNode import TreeNode


class LCA:

    @staticmethod
    def findLCA(tree, A, B):
        """

        :param tree: Tree or subtree we are to search
        :param A:   A value of a node in the tree
        :param B:   Value of another node's in the tree
        If either A or B are not in the tree, the LCA is that node
        """

        if tree is None or A == tree.data or B == tree.data:
            return tree

        leftTree = LCA.findLCA(tree.left, A, B)
        rightTree = LCA.findLCA(tree.right, A, B)

        if leftTree is None and rightTree is None:
            return None

        if leftTree is not None and rightTree is not None:
            return tree

        if leftTree is None:
            return rightTree
        else:
            return leftTree
