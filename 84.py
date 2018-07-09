def main():
    my_str=input().split()
    pre=my_str[0]
    n=int(my_str[1])
    for i in range(n-1):
        now=pre[0]
        my_len=1
        next=''
        for j in range(1,len(pre)):
            if pre[j]==now:
                my_len+=1
            else:
                next+=now+str(my_len)
                now=pre[j]
                my_len=1
        next+=now+str(my_len)
        pre=next
    print(pre)
if __name__ == '__main__':
    main()
