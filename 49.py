def main():
    n=int(input())
    sum=0
    my_array=input().split()
    for i in range(n):
        if i*2<=n-1:
            j=i
        else:
            j=n-1-i
        sum+=float(my_array[i])*(n-j)*(j+1) #reference to 49.png
    print('%.2f' % sum)
if __name__ == '__main__':
    main()
