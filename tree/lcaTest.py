import unittest

from lca import LCA
from treeNode import TreeNodeV1, TreeNodeV2, DAG

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
G = DAG()
a = TreeNodeV2('A')
b = TreeNodeV2('B')
c = TreeNodeV2('C')
d = TreeNodeV2('D')
e = TreeNodeV2('E')
f = TreeNodeV2('F')
g = TreeNodeV2('G')
a.addChildren((b, c))
b.addChildren(d)
c.addChildren((d, e, f))
d.addChildren(g)
e.addChildren(g)

G.add(a)
G.add(b)
G.add(c)
G.add(d)
G.add(e)
G.add(f)
G.add(g)

'''
    graph = {'A': {'B', 'C'},
             'B': {'D'},
             'C': {'D', 'E', 'F'},
             'D': {'G'},
             'E': {'G'},
             'F': {},
             'G': {}
             }
'''


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
        self.assertEqual(LCA.findLcaV2(G, d, f), 'C')
        self.assertEqual(LCA.findLcaV2(G, g, a), 'A')
        self.assertEqual(LCA.findLcaV2(G, d, g), 'D')
        self.assertEqual(LCA.findLcaV2(G, b, f), 'A')
        self.assertEqual(LCA.findLcaV2(G, e, d), 'C')

    def testBrokenV2(self):
        with self.assertRaises(TypeError) as context:
            LCA.findLcaV2('A', 1, None)
            LCA.findLcaV2(None, 1, 'SSD')
            self.assertIsNone(LCA.findLcaV2(G, TreeNodeV2(128), b))
            self.assertIsNone(LCA.findLcaV2(G, None, a))


if __name__ == "__main__":
    unittest.main()
