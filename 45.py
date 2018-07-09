def main():
    n=int(input())
    my_str=input().split()
    my_nums=[0]*n
    my_results=[0]*n
    for i in range(n):
        my_nums[i]=int(my_str[i])

    left_greater=[my_nums[0]]*n
    for i in range(1,n):
        if my_nums[i]>left_greater[i-1]:
            left_greater[i]=my_nums[i]
        else:
            left_greater[i]=left_greater[i-1]
    right_greater=[my_nums[n-1]]*n
    for i in range(n-2,-1,-1):
        if my_nums[i]<right_greater[i+1]:
            right_greater[i]=my_nums[i]
        else:
            right_greater[i]=right_greater[i+1]

    my_len=0
    for i in range(n):
        if right_greater[i]==my_nums[i] and left_greater[i]==my_nums[i]:
            my_results[my_len]=my_nums[i]
            my_len+=1

    print(my_len)
    for i in range(my_len-1):
        print(my_results[i],end=' ')
    if my_len>0:
        print(my_results[my_len-1])
    else:
        print()

if __name__ == '__main__':
    main()
