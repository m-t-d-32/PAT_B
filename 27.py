def main():
    my_str=input().split()
    my_num=int(my_str[0])
    my_char=my_str[1]

    all_use=-1
    now_use=0
    while (all_use<=my_num):
        now_use+=1
        all_use+=(2*now_use-1)*2
    all_use-=(2*now_use-1)*2
    now_use-=1
    for i in range(now_use):
        print(' '*i,end='')
        print(my_char*(2*now_use-1-2*i))
    for i in range(now_use-2,-1,-1):
        print(' '*i,end='')
        print(my_char*(2*now_use-1-2*i))
    print(my_num-all_use)
if __name__ == '__main__':
    main()
