class Node:
    data=None
    next=None
    def __init__(self,data):
        self.data=data

def Traversal(ptr):
    while ptr!=None:
        print(ptr.data)
        ptr=ptr.next

def insertionATB(ptr,data):
    newnode=Node(data)
    newnode.next=ptr
    return newnode

def insertionATEND(ptr,data):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        return newnode

    qtr=ptr
    ftr=qtr.next
    while ftr!=None:
        qtr=qtr.next
        ftr=ftr.next
    
    newnode=Node(data)
    newnode.next=None
    qtr.next=newnode
    return ptr

def insertionATBT(ptr,data,index):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        return newnode
    if index==0:
        newnode=Node(data)
        newnode.next=ptr
        return newnode
    count=0
    copyptr=ptr
    while copyptr!=None:
        count=count+1
        copyptr=copyptr.next

    if count>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index-1:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1
        newnode=Node(data)
        newnode.next=ftr
        qtr.next=newnode
        return ptr
    else:
        print("Index Out Of The Range")
        return ptr


def insertionATSVB(ptr,data,sval):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        return newnode
    if ptr.data==sval:
        newnode=Node(data)
        newnode.next=ptr
        return newnode
    flag=False
    copyptr=ptr
    while copyptr!=None:
        if copyptr.data==sval:
            flag=True
            break
        copyptr=copyptr.next

    if flag==True:
        qtr=ptr
        ftr=qtr.next
        while ftr.data!=sval:
            qtr=qtr.next
            ftr=ftr.next
        newnode=Node(data)
        newnode.next=ftr
        qtr.next=newnode
        return ptr
    else:
        print("Search Value Not Found")
        return ptr


def insertionATSVA(ptr,data,sval):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        return newnode
    flag=False
    copyptr=ptr
    while copyptr!=None:
        if copyptr.data==sval:
            flag=True
            break
        copyptr=copyptr.next

    if flag==True:
        qtr=ptr
        ftr=qtr.next
        while qtr.data!=sval:
            qtr=qtr.next
            ftr=ftr.next
        newnode=Node(data)
        newnode.next=ftr
        qtr.next=newnode
        return ptr
    else:
        print("Search Value Not Found")
        return ptr
    
    





a=None

a=insertionATEND(a,10)
a=insertionATEND(a,20)
a=insertionATEND(a,30)
a=insertionATEND(a,40)

a=insertionATBT(a,5,0)
a=insertionATBT(a,50,4)
a=insertionATBT(a,60,2)
a=insertionATSVA(a,15,5)
a=insertionATSVA(a,400,40)
Traversal(a)

