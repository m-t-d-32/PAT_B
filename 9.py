def main():
    str=input().split()
    for i in range(len(str)-1,0,-1):
        print(str[i],end=' ')
    print(str[0])
if __name__ == '__main__':
    main()
