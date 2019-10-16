from treeNode import TreeNodeV1, TreeNodeV2


class LCA:

    @staticmethod
    def findLcaV1(tree, A, B):
        """

        :param tree: Binary Tree or subtree we are to search
        :param A:   A value of a node in the tree
        :param B:   Value of another node's in the tree
        If either A or B are not in the tree, the LCA is that node
        """

        if tree is None or A == tree.data or B == tree.data:
            return tree

        leftTree = LCA.findLcaV1(tree.left, A, B)
        rightTree = LCA.findLcaV1(tree.right, A, B)

        if leftTree is None and rightTree is None:
            return None

        if leftTree is not None and rightTree is not None:
            return tree

        if leftTree is None:
            return rightTree
        else:
            return leftTree

    @staticmethod
    def findLcaV2(tree, A, B):
        """

        :param tree: Directed Acyclic Graph we are searching
        :param A: A value of a node in the graph
        :param B: Another value of a node in the graph
        """
        return TreeNode2(data=None)


