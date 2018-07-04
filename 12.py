def do1(k):
    sum=0
    for i in k:
        if i%2==0:
            sum+=i
    if sum==0:
        print('N',end=' ')
    else:
        print(sum,end=' ')

def do2(k):
    if (len(k)==0):
        print('N',end=' ')
    else:
        sum=0
        sel=1
        for i in k:
            sum+=sel*i;
            sel=-sel
        print(sum,end=' ')

def do3(k):
    if (len(k)==0):
        print('N',end=' ')
    else:
        print(len(k),end=' ')

def do4(k):
    if (len(k)==0):
        print('N',end=' ')
    else:
        avg=0
        for i in k:
            avg+=i
        avg/=len(k)
        print('%.1f' % avg,end=' ')

def do5(k):
    if (len(k)==0):
        print('N')
    else:
        max=-1
        for i in k:
            if i>max:
                max=i
        print(max)

def main():
    my_nums=input().split()
    k=[[],[],[],[],[]]
    for i in range(1,len(my_nums)):
        num=int(my_nums[i])
        k[num%5].append(num)
    do1(k[0])
    do2(k[1])
    do3(k[2])
    do4(k[3])
    do5(k[4])

if __name__ == '__main__':
    main()
