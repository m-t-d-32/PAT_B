def main():
    my_str=input().split()
    m=int(my_str[0])
    n=int(my_str[1])
    s=int(my_str[2])
    s-=1

    count=0
    priced=dict()
    price_num=0
    for i in range(m):
        my_str=input()
        if my_str not in priced or priced[my_str]==False:
            if count>=s and (count-s)%n==0:
                print(my_str)
                price_num+=1
                priced[my_str]=True
            else:
                priced[my_str]=False
            count+=1
    if price_num==0:
        print('Keep going...')
if __name__ == '__main__':
    main()
