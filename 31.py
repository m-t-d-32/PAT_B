def main():
    n=int(input())
    const_key=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    const_chk=['1','0','X','9','8','7','6','5','4','3','2']
    unpassed=[]
    for i in range(n):
        my_str=input()
        sum=0
        now_value=True
        for j in range(len(my_str)-1):
            if my_str[j]>='0' and my_str[j]<='9':
                sum+=const_key[j]*int(my_str[j])
            else:
                now_value=False
                break
        sum%=11
        if now_value==False or const_chk[sum]!=my_str[-1]:
            unpassed.append(my_str)
    if len(unpassed)==0:
        print('All passed')
    else:
        for i in unpassed:
            print(i)
if __name__ == '__main__':
    main()
