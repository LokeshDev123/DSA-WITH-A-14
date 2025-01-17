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
    qtr=ptr
    ftr=qtr.next
    while ftr!=None:
        ftr=ftr.next
        qtr=qtr.next
    newnode=Node(data)
    newnode.next=None
    qtr.next=newnode
    return ptr


def insertionATBT(ptr,data,index):
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

def insertionATSVB(ptr,data,sval):
    qtr=ptr
    ftr=qtr.next
    while ftr.data!=sval:
        qtr=qtr.next
        ftr=ftr.next
    newnode=Node(data)
    newnode.next=ftr
    qtr.next=newnode
    return ptr

a=Node(10)
b=Node(20)
c=Node(30)
d=Node(40)

a.next=b
b.next=c
c.next=d
d.next=None

a=insertionATB(a,50)
a=insertionATB(a,60)
a=insertionATEND(a,100)
a=insertionATEND(a,120)
a=insertionATBT(a,200,6)
a=insertionATSVB(a,300,200)
Traversal(a)