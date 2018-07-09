def main():
    every_radix=input()[::-1]
    add1=input()[::-1]
    add2=input()[::-1]
    if len(add1)>len(add2):
        add2+='0'*(len(add1)-len(add2))
    else:
        add1+='0'*(len(add2)-len(add1))
    my_sum=[0]*len(every_radix)
    carry=0
    for i in range(len(every_radix)):
        now_bit=int(add1[i])+int(add2[i])+carry
        divide=int(every_radix[i])
        if divide==0:
            divide=10
        carry=now_bit//divide
        now_bit%=divide
        my_sum[i]=now_bit
    print_count=len(every_radix)
    if carry!=0:
        my_sum.append(carry)
        print_count+=1
    now_print=False
    my_sum=my_sum[::-1]
    for i in range(print_count):
        if my_sum[i]!=0 or i==print_count-1:
            now_print=True
        if now_print:
            print(my_sum[i],end='')
if __name__ == '__main__':
    main()
