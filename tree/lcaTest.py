import unittest

from lca import LCA
from treeNode import TreeNodeV1, TreeNodeV2

Tv1 = TreeNodeV1(3)
Tv1.left = TreeNodeV1(2)
Tv1.left.left = TreeNodeV1(1)
Tv1.left.left.left = TreeNodeV1(0.2)
Tv1.left.right = TreeNodeV1(2.5)
Tv1.right = TreeNodeV1(4)
Tv1.right.right = TreeNodeV1(8)

'''
            3
          /   \
         2     4
        / \     \
       1   2.5   8     
      / 
     0.2   
'''

a = TreeNodeV2('A')
b = TreeNodeV2('B')
c = TreeNodeV2('C')
d = TreeNodeV2('D')
e = TreeNodeV2('E')
f = TreeNodeV2('F')
g = TreeNodeV2('G')
a.children = {b, c}
b.children = {d}
c.children = {d, e, f}
d.children = {g}
e.children = {g}
f.children = {}
g.children = {}


class LCATester(unittest.TestCase):
    def testLcaV1(self):
        self.assertEqual(LCA.findLcaV1(Tv1, 1, 2.5).data, 2)
        self.assertEqual(LCA.findLcaV1(Tv1, 3, 3).data, 3)
        self.assertEqual(LCA.findLcaV1(Tv1, 8, 2.5).data, 3)
        self.assertEqual(LCA.findLcaV1(Tv1, 4, 3).data, 3)
        self.assertEqual(LCA.findLcaV1(Tv1, 10, 2).data, 2)
        self.assertEqual(LCA.findLcaV1(Tv1, 2, 1).data, 2)
        self.assertEqual(LCA.findLcaV1(Tv1, 8, 0.2).data, 3)

    def testBrokenV1(self):
        self.assertEqual(LCA.findLcaV1(Tv1, 1, None).data, 1)
        self.assertIsNone(LCA.findLcaV1(None, 1, 2.5))
        self.assertIsNone(LCA.findLcaV1(Tv1, None, None))
        self.assertIsNone(LCA.findLcaV1(None, None, None))

    def testLcaV2(self):
        self.assertEqual(LCA.findLcaV2('A', 'D', 'F').data, 'C')
        self.assertEqual(LCA.findLcaV2('A', 'G', 'A').data, 'A')
        self.assertEqual(LCA.findLcaV2('A', 'D', 'G').data, 'D')
        self.assertEqual(LCA.findLcaV2('A', 'B', 'F').data, 'A')
        self.assertEqual(LCA.findLcaV2('A', 'E', 'D').data, 'C')

    def testBrokenV2(self):
        self.assertIsNone(LCA.findLcaV2('A', 1, None))
        self.assertIsNone(LCA.findLcaV2(None, 1, 2.5))
        self.assertIsNone(LCA.findLcaV2('A', None, None))
        self.assertIsNone(LCA.findLcaV2(None, None, None))


if __name__ == "__main__":
    unittest.main()
