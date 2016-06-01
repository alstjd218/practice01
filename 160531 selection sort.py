def selectionSort(alist):
    for start in range(len(alist)-1):
        positionOfMin=start
        for i in range(start,len(alist)):
            if alist[i]<alist[positionOfMin]:
                positionOfMin=i
        alist[start],alist[positionOfMin]=alist[positionOfMin],alist[start]
        print alist
 

a=str.split(raw_input('Input any integers(separate numbers with spacing) : '))
for i in range(len(a)):
    a[i]=int(a[i])
selectionSort(a)
