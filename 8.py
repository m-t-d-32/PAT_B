class Node:
    def __init__(self):
        self.prior=None
        self.next=None
        self.value=0
class LinkedList:
    def __init__(self,n):
        self.head=Node()
        ptr=self.head
        my_array=input().split()
        for i in range(n-1):
            ptr.value=int(my_array[i])
            ptr.next=Node()
            ptr.next.prior=ptr
            ptr=ptr.next
        ptr.value=int(my_array[n-1])
        self.tail=ptr
    def pop_back(self):
        value=self.tail.value
        self.tail=self.tail.prior
        self.tail.next=None
        return value
    def push_front(self,value):
        temp=Node()
        temp.value=value
        temp.next=self.head
        self.head.prior=temp
        self.head=temp
    def print(self):
        ptr=self.head
        while ptr!=self.tail:
            print(ptr.value,end=' ')
            ptr=ptr.next
        print(ptr.value)
def main():
    my_input=input().split()
    n=int(my_input[0])
    m=int(my_input[1])

    ll=LinkedList(n)
    for i in range(m):
        value=ll.pop_back()
        ll.push_front(value)
    ll.print()
if __name__ == '__main__':
    main()
