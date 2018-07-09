def main():
    n=int(input())
    lines=input().split()
    for i in range(n):
        lines[i]=int(lines[i])
    lines.sort()
    sum=lines[0]
    for i in range(1,n):
        sum+=lines[i]
        sum/=2
    print(int(sum))
if __name__ == '__main__':
    main()
