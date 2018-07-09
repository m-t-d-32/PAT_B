def main():
    n=int(input())
    my_results=set()
    my_str=input().split()
    for i in range(n):
        temp_str=my_str[i]
        sum=0
        for i in temp_str:
            sum+=int(i)
        my_results.add(sum)
    results=list(my_results)
    results.sort()
    my_len=len(results)
    print(my_len)
    for i in range(my_len-1):
        print(results[i],end=' ')
    print(results[my_len-1])
if __name__ == '__main__':
    main()
