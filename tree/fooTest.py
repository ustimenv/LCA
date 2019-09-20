import unittest

from tree.foo import Foo


class FooTester(unittest.TestCase):

    def setUp(self):
        self.F = Foo()

    def testAdd(self):
        self.assertEqual(self.F.add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
