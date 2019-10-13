import unittest

from lca import LCA
from treeNode import TreeNode

T = TreeNode(3)
T.left = TreeNode(2)
T.left.left = TreeNode(1)
T.left.left.left = TreeNode(0.2)
T.left.right = TreeNode(2.5)
T.right = TreeNode(4)
T.right.right = TreeNode(8)

'''
            3
          /   \
         2     4
        / \     \
       1   2.5   8     
      / 
     0.2   
'''


class LCATester(unittest.TestCase):
    def testLCA(self):
        self.assertEqual(LCA.findLCA(T, 1, 2.5).data, 2)
        self.assertEqual(LCA.findLCA(T, 3, 3).data, 3)
        self.assertEqual(LCA.findLCA(T, 8, 2.5).data, 3)
        self.assertEqual(LCA.findLCA(T, 4, 3).data, 3)
        self.assertEqual(LCA.findLCA(T, 10, 2).data, 2)
        self.assertEqual(LCA.findLCA(T, 2, 1).data, 2)
        self.assertEqual(LCA.findLCA(T, 8, 0.2).data, 3)

    def testBroken(self):
        self.assertEqual(LCA.findLCA(T, 1, None).data, 1)
        self.assertIsNone(LCA.findLCA(None, 1, 2.5))
        self.assertIsNone(LCA.findLCA(T, None, None))
        self.assertIsNone(LCA.findLCA(None, None, None))


if __name__ == "__main__":
    unittest.main()
