def main():
    my_num=int(input())
    B_num=my_num//100
    for i in range(B_num):
        print('B',end='')
    my_num%=100
    S_num=my_num//10
    for i in range(S_num):
        print('S',end='')
    my_num%=10
    for i in range(1,my_num+1):
        print(i,end='')
if __name__ == '__main__':
    main()
