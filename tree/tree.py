
class Tree:

    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

    def addChild(self, child='left', data=None):
        pass

    def removeChild(self, child='right'):
        try:
            assert child == 'left' or child == 'right'
            eval('self.' + child + ' = None')

        except Exception:
            print(Exception)

    def __repr__(self):
        pass

    def __str__(self):
        pass