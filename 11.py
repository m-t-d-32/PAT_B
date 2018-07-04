def main():
    n=int(input())
    for i in range(n):
        sstr=input().split()
        if int(sstr[0])+int(sstr[1])>int(sstr[2]):
            print('Case #'+str(i+1)+": true")
        else:
            print('Case #'+str(i+1)+": false")
if __name__ == '__main__':
    main()
