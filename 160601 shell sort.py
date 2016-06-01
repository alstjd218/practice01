def shellSortFinal(alist):
    numOfSublist=len(alist)//2
    while numOfSublist>=1:
        increment=numOfSublist
        shellSort(alist,increment)
        print 'increment :',increment, alist
        numOfSublist=numOfSublist//2
        
    
def shellSort(alist,increment):
    for start in range(increment):
        for i in range(start+increment,len(alist),increment):
            comparisonItem=alist[i]
            position=i-increment
            while alist[position]>comparisonItem and position>=0:
                alist[position+increment]=alist[position]
                position=position-increment
                
            alist[position+increment]=comparisonItem
                
     




a=str.split(raw_input('Input any integers(separate numbers with spacing) : '))
for i in range(len(a)):
    a[i]=int(a[i])
shellSortFinal(a)


