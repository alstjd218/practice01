def shortBubbleSort(alist):
    sortedList=False
    for passnum in range(len(alist)-1,0,-1):
        if sortedList==False:
            sortedList=True
            for i in range(passnum):
                if alist[i]>alist[i+1]:
                    alist[i],alist[i+1]=alist[i+1],alist[i]
                    sortedList=False


a=str.split(raw_input('Input any integers(separate numbers with spacing) : '))
for i in range(len(a)):
    a[i]=int(a[i])
shortBubbleSort(a)
print a
