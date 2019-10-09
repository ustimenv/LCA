import unittest

from lca import LCA
from tree import Node


class LCATester(unittest.TestCase):

    def setUp(self):
        self.L = LCA()
        self.N = Node()

    def testLCA(self):
        pass

    def testBroken(self):
        pass

    def testOnSelf(self):
        pass

    def testInvalidInput(self):
        pass

if __name__ == "__main__":
    unittest.main()
