
class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return '('+str(self.data)+')'


if __name__ == "__main__":
    N = Node(1)
    N.left = 3
    print(N)

