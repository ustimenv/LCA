
class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __eq__(self, other):
        return  self.data == other.data and \
                self.left == other.left and \
                self.right == other.right

