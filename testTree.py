import unittest
from tree import *

class testHuffmanTree(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_btree_root(self):
        root=TreeNode()
        htree=HuffmanTree(root)
        self.assertEqual(htree.builtTree(),{'h':1,'e':1,'l':2,'o':1})
    
if __name__ =='__main__':  
    unittest.main()
