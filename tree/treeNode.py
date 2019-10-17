
class TreeNodeV1:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __eq__(self, other):
        return  self.data == other.data and \
                self.left == other.left and \
                self.right == other.right


class TreeNodeV2:
    def __init__(self, data=None):
        self.data = data
        self.children = []
        self.parents = []

    def addChildren(self, children):
        if isinstance(children, TreeNodeV2):
            self.children.append(children)
        else:
            for child in children:
                self.children.append(child)

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)


class DAG:
    def __init__(self):
        self.nodes = set()
        self.root = None

    def add(self, X):
        if len(self.nodes) < 1:
            self.root = X
        self.nodes.add(self.root)



