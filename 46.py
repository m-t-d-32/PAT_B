def main():
    n=int(input())
    wine_a=0
    wine_b=0
    for i in range(n):
        my_str=input().split()
        ax=int(my_str[0])
        ay=int(my_str[1])
        bx=int(my_str[2])
        by=int(my_str[3])

        if ay==ax+bx and by!=ax+bx:
            wine_b+=1
        elif ay!=ax+bx and by==ax+bx:
            wine_a+=1
    print(str(wine_a)+' '+str(wine_b))
if __name__ == '__main__':
    main()
