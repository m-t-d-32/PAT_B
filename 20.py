def main():
    my_str=input().split()
    my_type=int(my_str[0])
    my_need=int(my_str[1])

    weights=[]
    all_prices=[]
    every_prices=[]
    my_str=input().split()
    for i in range(my_type):
        weights.append(int(my_str[i]))
    my_str=input().split()
    for i in range(my_type):
        all_prices.append(int(my_str[i]))
        every_prices.append(all_prices[i]/weights[i])
        '''
    for i in range(my_type-1,-1,-1):
        for j in range(i):
            if every_prices[j]<every_prices[j+1]:
                every_prices[j],every_prices[j+1]=every_prices[j+1],every_prices[j]
                weights[j],weights[j+1]=weights[j+1],weights[j]
                all_prices[j],all_prices[j+1]=all_prices[j+1],all_prices[j]
        '''
    sum=0
    for i in range(my_type):
        if my_need>=weights[i]:
            my_need-=weights[i]
            sum+=all_prices[i]
        else:
            sum+=every_prices[i]*my_need
            break
    print("%.2f" % sum)

if __name__ == '__main__':
    main()
