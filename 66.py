def my_print(color,begin,end,color_default):
    if color>=begin and color<=end:
        print("%03d" % color_default,end='')
    else:
        print("%03d" % color,end='')
def main():
    my_str=input().split()
    n=int(my_str[0])
    m=int(my_str[1])
    begin=int(my_str[2])
    end=int(my_str[3])
    replace=int(my_str[4])
    for i in range(n):
        my_str=input().split()
        for j in range(m-1):
            my_print(int(my_str[j]),begin,end,replace)
            print(' ',end='')
        my_print(int(my_str[m-1]),begin,end,replace)
        print()
if __name__ == '__main__':
    main()
