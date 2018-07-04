def main():
    my_str=input().split()
    result=''
    if my_str[0]!='0':
        for i in range(1,len(my_str)):
            if my_str[i]!='0':
                my_str[i]=str(int(my_str[i])-1)
                result+=str(i)
                break
    for i in range(len(my_str)):
        while my_str[i]!='0':
            result+=str(i)
            my_str[i]=str(int(my_str[i])-1)
    print(result)
if __name__ == '__main__':
    main()
