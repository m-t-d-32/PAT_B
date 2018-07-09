def main():
    my_pair=[100004]*100005
    has_come=[False]*100005
    n=int(input())
    for i in range(n):
        my_str=input().split()
        he=int(my_str[0])
        she=int(my_str[1])
        my_pair[he]=she
        my_pair[she]=he
    m=int(input())
    my_str=input().split()
    for i in range(m):
        my_str[i]=int(my_str[i])
        has_come[my_str[i]]=True
    results=[]
    for i in range(m):
        if has_come[my_pair[my_str[i]]]==False:
            results.append(my_str[i])
    results.sort()
    print(len(results))
    for i in range(len(results)-1):
        print(results[i],end=' ')
    if (len(results)!=0):
        print(results[len(results)-1])
if __name__ == '__main__':
    main()
