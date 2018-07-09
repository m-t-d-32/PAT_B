def main():
    my_str=input()
    sum=0
    for i in my_str:
        if i>='A' and i<='Z':
            sum+=ord(i)-ord('A')+1
        elif i>='a' and i<='z':
            sum+=ord(i)-ord('a')+1
    sum_key=[0,0]
    while sum!=0:
        sum_key[sum & 1]+=1
        sum>>=1
    print(str(sum_key[0])+' '+str(sum_key[1]))
if __name__=='__main__':
    main()