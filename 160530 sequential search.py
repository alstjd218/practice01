def sequentialSearch(alist,item):
    position=0
    while position<len(alist):
        if item==alist[position]:
            return 1
        else:
            position+=1

    return 0



def orderedSequentialSearch(alist,item):
    position=0
    while position<len(alist):
        if item==alist[position]:
            return 1
        else:
            if item>alist[position]:
                position+=1
            else:
                return 0

    return 0




num1=int(raw_input('Input any natural number N between 1 and 100000 : '))
a=str.split(raw_input('Input any N integers : '))
num2=int(raw_input('Input any natural number M between 1 and 100000 : '))
b=str.split(raw_input('Input any M integers : '))



for item in b:
    print sequentialSearch(a,item)
         
print ''


a.sort()
for item in b:
    print orderedSequentialSearch(a,item)
         

