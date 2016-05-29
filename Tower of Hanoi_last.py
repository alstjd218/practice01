a,b,c=1,2,3
result=[]

def moves(a,b,c,num):
    if num==1:
        result=[a,c]
        return result


def moves(a,b,c,num):
    if num>=1:
        moves(a,c,b,num-1)
        result.append(a)
        result.append(c)
        moves(b,a,c,num-1)

    
def countOfMoves(num):
    count=0
    for k in range(num):
        count+=count+1
    return count


numOfDisk=int(raw_input('Input the number of disks : '))
print countOfMoves(numOfDisk)

if numOfDisk<20:
    moves(a,b,c,numOfDisk)
    for k in range(len(result)/2):
        print result[2*k],result[2*k+1]
