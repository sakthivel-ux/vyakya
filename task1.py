
ida=[]
idb=[]

oda=[]
odb=[]

def subsetSums(arr, l, r,b,curra,currb,sum=0):
    if l > r:
        if(b==0):
            oda.append(curra.copy())
            ida.append(sum)
#            print("curra: ",curra,sum)
        elif(b==1):
            if(sum not in idb):
                odb.append(currb.copy())
                idb.append(sum)
#            print("currb: ",currb,sum)
        return
    if(b==0):
        curra.append(arr[l])
    else:
        currb.append(arr[l])
    subsetSums(arr, l + 1, r,b,curra,currb,sum + arr[l])
    if(b==0):
        curra.pop()
    else:
        currb.pop()
    subsetSums(arr, l + 1, r,b,curra,currb, sum)

def solve(alist:list,blist:list)->None:
    n=len(alist)
    b=0
    curra=[]
    currb=[]
    subsetSums(alist, 0, n - 1,b,curra,currb)
    n=len(blist)
    b=1
    subsetSums(blist, 0, n - 1,b,curra,currb)
    aval=len(ida)
    bval=len(idb)
    flag=0
    print()
    for elei in idb:
        for elej in ida:
            if(elei==elej):
                print(odb[idb.index(elei)])
                print()
                for i in range(0,len(ida)):
                    if(ida[i]==elej):
                        print(oda[i])
                flag=1
                break
        if(flag==1):
            break
    if(flag==0):
        print(0)
    
if __name__ == '__main__':
    print("enter the number of elements in A List")
    a=int(input());
    alist=[]
    blist=[]
    print("enter",a,"elements ")
    for i in range(0,a):
        val=int(input())
        alist.append(val)
    print("enter the number of elements in B List")
    b=int(input())
    print("enter",b,"elements ")
    for i in range(0,b):
        val=int(input())
        blist.append(val)
    for ele in blist:
        idb.append(ele)
        odb.append([ele])
    solve(alist,blist)
    