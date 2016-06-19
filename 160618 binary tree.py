def binaryTree(root):
    return [root,[],[]]

def insertLeft(root,newBranch):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,t,[]])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

    
def buildTree():
    tree=binaryTree('a')
    insertLeft(tree,'b')
    insertLeft(getLeftChild(tree),'d')
    insertRight(tree,'c')
    insertLeft(getRightChild(tree),'e')
    insertRight(getRightChild(tree),'f')
    return tree


    
print buildTree()
