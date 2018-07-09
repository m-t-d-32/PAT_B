class MoonCake:
    def __init__(self,weight,all_price):
        self.weight=weight
        self.all_price=all_price
        self.every_price=all_price/weight
def get_key(mooncake):
    return mooncake.every_price
def main():
    my_str=input().split()
    my_type=int(my_str[0])
    my_need=int(my_str[1])

    mooncakes=[None]*my_type
    my_str=input().split()
    myx_str=input().split()
    for i in range(my_type):
            weight=float(my_str[i])
            all_price=float(myx_str[i])
            mooncakes[i]=MoonCake(weight,all_price)
    mooncakes.sort(key=get_key,reverse=True)

    sum=0
    for i in range(my_type):
        if my_need>=mooncakes[i].weight:
            my_need-=mooncakes[i].weight
            sum+=mooncakes[i].all_price
        else:
            sum+=mooncakes[i].every_price*my_need
            break
    print("%.2f" % sum)

if __name__ == '__main__':
    main()
