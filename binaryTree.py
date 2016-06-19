class BinaryTree:
    def __init__(self,rootVal):
        self.key=rootVal
        self.leftChild=None
        self.rightChild=None


    def insertLeft(self,factor):
        if self.leftChild==None:
            self.leftChild=BinaryTree(factor)
        else:
            child=BinaryTree(factor)
            child.leftChild=self.leftChild
            self.leftChild=child

    def insertRight(self,factor):
        if self.rightChild==None:
            self.rightChild=BinaryTree(factor)
        else:
            child=BinaryTree(factor)
            child.rightChild=self.rightChild
            self.rightChild=child

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild
    
 
    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
