def main():
    n=int(input())
    my_str=input().split()
    counts=[0]*len(my_str)
    for i in range(len(my_str)):
        result=i-int(my_str[i])+1
        if result<0:
            result=-result
        counts[result]+=1
    for i in range(len(counts)-1,-1,-1):
        if counts[i]>1:
            print(str(i)+' '+str(counts[i]))
if __name__ == '__main__':
    main()
