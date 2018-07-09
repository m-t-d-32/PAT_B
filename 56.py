#PAT 判题系统输入与题目不符，只输入一行，因此代码如下
def main():
    my_str=input().split()
    n=int(my_str[0])
    sum=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i!=j):
                sum+=int(my_str[i]+my_str[j])
    print(sum)
if __name__=='__main__':
    main()