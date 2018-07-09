def main():
    my_str=input().split('E')
    front=''
    for i in my_str[0][1:]:
        if i!='.':
            front+=i
    back=int(my_str[1])
    if my_str[0][0]=='-':
        print('-',end='')
    if back>=0:
        if len(front)>back+1:
            for i in range(back+1):
                print(front[i],end='')
            print('.',end='')
            for i in range(back+1,len(front)):
                print(front[i],end='')
        else:
            print(front,end='')
            for i in range(back+1-len(front)):
                print('0',end='')
        print()
    else:
        print('0.',end='')
        for i in range(-back-1):
            print('0',end='')
        print(front)
if __name__ == '__main__':
    main()
