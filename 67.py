def main():
    my_str=input().split()
    pwd=my_str[0]
    try_max=int(my_str[1])
    try_count=0
    while True:
        my_str=input()
        if try_count>=try_max:
            print('Account locked')
            break
        elif my_str=='#':
            break
        elif my_str==pwd:
            print('Welcome in')
            break
        else:
            print('Wrong password: '+my_str)
            try_count+=1

if __name__ == '__main__':
    main()
