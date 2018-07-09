import math
def prime(rank):
    for i in range(2,int(math.sqrt(rank))+1):
        if rank%i==0:
            return False
    return True
def main():
    n=int(input())
    students=dict()
    for i in range(n):
        num=int(input())
        students[num]=i+1
    m=int(input())
    for i in range(m):
        num=int(input())
        print("%04d: " % num,end='')
        if num in students:
            rank=students[num]
            if rank==1:
                print('Mystery Award')
            elif rank==-1:
                print('Checked')
            elif prime(rank):
                print('Minion')
            else:
                print('Chocolate')
            students[num]=-1
        else:
            print('Are you kidding?')
if __name__ == '__main__':
    main()
