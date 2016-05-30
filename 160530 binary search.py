def binarySearch(alist,item):
    if len(alist)==0:
        return 0
    else:
        midpoint=len(alist)//2
        if item==alist[midpoint]:
            return 1
        else:
            if item>alist[midpoint]:
                return binarySearch(alist[midpoint+1:],item)
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)





num1=int(raw_input('Input any natural number N between 1 and 100000 : '))
a=str.split(raw_input('Input any N integers : '))
num2=int(raw_input('Input any natural number M between 1 and 100000 : '))
b=str.split(raw_input('Input any M integers : '))
a.sort()


for item in b:
    print binarySearch(a,item)
         

