def Judge(n):
    i=0
    j=len(n)-1
    while i<j:
        if n[i]!=n[j]:
            return False
        i+=1
        j-=1
    return True
def main():
    n=input()
    count=0
    while not Judge(n) and count<10:
        n1=int(n)
        n2=int(n[::-1])
        n=str(n1+n2)
        print(str(n1)+' + '+str(n2)+' = '+n)
        count+=1
    if Judge(n):
        print(n+' is a palindromic number.')
    else:
        print('Not found in 10 iterations.')
if __name__ == '__main__':
    main()
