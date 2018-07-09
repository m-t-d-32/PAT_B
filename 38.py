#PTA超时，牛客网通过，牛客网输入一行，因此代码有所修改。牛客网：https://www.nowcoder.com/questionTerminal/3df4810cc0664b8bb848d785f68f7c9b

##Code For PTA:

def main():
    n=int(input())
    basket=[0]*101
    my_str=input().split()
    for i in range(n):
        basket[int(my_str[i])]+=1
    my_str=input().split()
    if int(my_str[0])>0:
        for i in range(1,int(my_str[0])):
            print(basket[int(my_str[i])],end=' ')
        print(basket[int(my_str[int(my_str[0])])])
if __name__ == '__main__':
    main()

#Code For 牛客网:

def main():

    basket=[0]*101
    my_str=input().split()
    n=int(my_str[0])
    for i in range(1,n+1):
        basket[int(my_str[i])]+=1
    if int(my_str[n+1])>0:  #n+1 n+2
        for i in range(n+2,int(my_str[n+1])+n+1):
            print(basket[int(my_str[i])],end=' ')
        print(basket[int(my_str[int(my_str[n+1])+n+1])])
if __name__ == '__main__':
    main()
