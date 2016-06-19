"""  """

def moves(a,b,c,num):
    if num==1:
        print a,c
    else:
        moves(a,c,b,num-1)
        print a,c
        moves(b,a,c,num-1)
        
        
        
def countOfMoves(num):
    count=0
    for k in range(num):
        count = count*2+1
    return count


numOfDisk=int(raw_input('Input the number of disks : '))
print countOfMoves(numOfDisk)

a,b,c=1,2,3

if numOfDisk<20:
     moves(a,b,c,numOfDisk)

