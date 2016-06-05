def partition(alist):
    if len(alist)<=1:
        return alist
    else:
        pivot=alist[0]
        leftmark=1
        rightmark=len(alist)-1

        while True:
            while leftmark<len(alist) and alist[leftmark]<pivot:
                leftmark+=1

            while rightmark>0 and alist[rightmark]>pivot:
                rightmark+=-1

            if leftmark<rightmark:
                alist[leftmark],alist[rightmark]=alist[rightmark],alist[leftmark]
            else:
                alist[0], alist[rightmark]=alist[rightmark], pivot
                print alist

                leftside=alist[:rightmark]
                rightside=alist[rightmark+1:]
                

                partition(leftside)
                partition(rightside)

            
                return alist
                


alist=[54,26,93,17,77,31,44,55,20]
print partition(alist)
            
        
            
