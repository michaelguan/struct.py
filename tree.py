 #coding=utf-8
from collections import *
from queue import PriorityQueue

class TreeNode(object):
    '''
       define the node of the huffmantree
    '''
    def __init__(self,data='0',weight=0,parent=None,lchild=None,rchild=None):
        self.data=data
        self.weight=weight
        self.parent=parent
        self.lchild=lchild
        self.rchild=rchild
        
    def __lt__(self,node):
        return ord(self.data)<ord(node.data)
        
class HuffmanTree(object):
    queue=PriorityQueue()
    def __init__(self,root=None):
        self.root=root
    
    def buildTree(self,inputstring='hello'):
        nodes=[]
        for data,weight in dict(Counter(inputstring)).items():
            tnode=TreeNode(data=data,weight=weight)
            nodes.append(tnode)
            self.queue.put((weight,tnode))
        for i in range(len(nodes)-2):
            lchild=self.queue.get()[1]
            rchild=self.queue.get()[1]
            weight=lchild.weight+rchild.weight
            tnode1=TreeNode(data=str(i),weight=weight,lchild=lchild,rchild=rchild)
            self.queue.put(weight,tnode1)
        self.root=self.queue.get()[1]
        return self.queue
        
if __name__ =='__main__':
    htree=HuffmanTree()
    queue=htree.buildTree()
    while not queue.empty():
        print(queue.get()[1].weight)