from Stack_ import Stack
from binaryTree import BinaryTree




def parseTree(formula):
    alist=formula.split()
    aTree=BinaryTree('')
    pStack=Stack()
    current=aTree
    print aTree
    print alist
    for i in alist:
        if i=='(':
            current.insertLeft('')
            pStack.push(current)
            current=current.getLeftChild()
            
        elif i not in ['+','-','*','/',')']:
            current.setRootVal(i)
            parent=pStack.pop()
            current=parent
            
        elif i in ['+','-','*','/']:
            current.setRootVal(i)
            current.insertRight('')
            pStack.push(current)
            current=current.getRightChild()

        elif i ==')':
            current=pStack.pop()

    return aTree



a="( ( 10 + 5 ) * 3 )"

print parseTree(a)
