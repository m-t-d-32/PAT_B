def main():
    my_str=input().split()
    n=int(my_str[0])
    m=int(my_str[1])
    my_array=[0]*n

    my_str=input().split()
    for i in range(n):
        my_array[i]=int(my_str[i])
    my_array.sort()

    max_index=-1
    max_value=my_array[0]*m
    for i in range(n):
        if max_value<my_array[i]:
            max_index=i-1
            break
    if max_index==-1:
        max_index=n-1

    max_number=max_index
    i=0
    while i+max_number<n:
        if my_array[i]*m>=my_array[i+max_number]:
            while i+max_number<n and my_array[i]*m>=my_array[i+max_number]:
                max_number+=1
            max_number-=1
        i+=1
    print(max_number+1)
if __name__ == '__main__':
    main()
