def main():
    my_str=input().split()
    value1=my_str[0]
    key1=my_str[1]
    value2=my_str[2]
    key2=my_str[3]

    sum1=0
    for i in value1:
        if key1==i:
            sum1*=10
            sum1+=(int(key1))
    sum2=0
    for i in value2:
        if key2==i:
            sum2*=10
            sum2+=(int(key2))

    print(sum1+sum2)
if __name__ == '__main__':
    main()
