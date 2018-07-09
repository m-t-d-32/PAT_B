def main():
    my_str=input().split()
    my_len=int(my_str[0])
    my_char=my_str[1]

    print(my_char*my_len)
    for i in range(1,int(my_len/2+0.5)-1):
        print(my_char,end='')
        print(' '*(my_len-2),end='')
        print(my_char)
    print(my_char*my_len)
if __name__ == '__main__':
    main()
