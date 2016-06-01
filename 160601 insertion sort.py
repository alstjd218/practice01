def insertionSort(alist):
    for sublist in range(len(alist)-1):
        comparisonItem=alist[sublist+1]
        for sublistIndex in range(sublist,-1,-1):
            if alist[sublistIndex]>comparisonItem:
                alist[sublistIndex+1],alist[sublistIndex]=alist[sublistIndex],comparisonItem
        print alist


a=str.split(raw_input('Input any integers(separate numbers with spacing) : '))
for i in range(len(a)):
    a[i]=int(a[i])
insertionSort(a)
