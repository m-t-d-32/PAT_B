def main():
    operate=input()
    if operate=='C':
        my_str=input()
        now_bit=my_str[0]
        count=1
        for i in range(1,len(my_str)):
            if my_str[i]==now_bit:
                count+=1
            else:
                if count>1:
                    print(count,end='')
                print(now_bit,end='')
                now_bit=my_str[i]
                count=1
        if count>1:
            print(count,end='')
        print(now_bit,end='')
    else:
        my_str=input()
        count=1
        i=0
        while i<len(my_str):
            if my_str[i]>='0' and my_str[i]<='9':
                count=0
                while my_str[i]>='0' and my_str[i]<='9':
                    count=int(my_str[i])+count*10
                    i+=1
            else:
                print(my_str[i]*count,end='')
                count=1
                i+=1
if __name__ == '__main__':
    main()
