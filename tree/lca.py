from treeNode import TreeNodeV1, TreeNodeV2, DAG


class LCA:

    @staticmethod
    def findLcaV1(root, A, B):
        """

        :param root: Binary Tree or subtree we are to search
        :param A:   A value of a node in the tree
        :param B:   Value of another node's in the tree
        If either A or B are not in the tree, the LCA is that node
        """

        if root is None or A == root.data or B == root.data:
            return root

        leftTree = LCA.findLcaV1(root.left, A, B)
        rightTree = LCA.findLcaV1(root.right, A, B)

        if leftTree is None and rightTree is None:
            return None

        if leftTree is not None and rightTree is not None:
            return root

        if leftTree is None:
            return rightTree
        else:
            return leftTree

    @staticmethod
    def findPaths(g, A, B, path=[]):
        path = path + [A]
        if A == B:
            return [path]
        if A is None:
            return []
        paths = []

        for child in A.children:
            if child not in path:
                newpaths = LCA.findPaths(g, child, B, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    @staticmethod
    def findLcaV2(graph, A, B):
        if isinstance(graph, DAG) and isinstance(A, TreeNodeV2) and isinstance(B, TreeNodeV2):
            pass
        else:
            raise TypeError('Invalid input type')

        """

        :param graph: Directed Acyclic Graph we are searching
        :param A: A value of a node in the graph
        :param B: Another value of a node in the graph
        """

        nodesA = set()
        nodesB = set()
        for path in LCA.findPaths(graph, graph.root, A):
            for p in path:
                nodesA.add(p.data)

        for path in LCA.findPaths(graph, graph.root, B):
            for p in path:
                nodesB.add(p.data)



        try:
            return max(nodesA.intersection(nodesB))
        except:
            return None
