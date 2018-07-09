def main():
    n=int(input())
    my_str=input().split()
    for i in range(n):
        my_str[i]=int(my_str[i])
    my_str.sort(reverse=True)

    printed=False
    for i in range(n):
        if i+1>=my_str[i]:
            print(i)
            printed=True
            break
    if printed==False:
        print(n)
if __name__ == '__main__':
    main()
