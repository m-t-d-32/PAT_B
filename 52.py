def get():
    my_str=input()
    begin=False
    tmp_str=''
    ret_str=[]
    for i in my_str:
        if i=='[':
            begin=True
            tmp_str=''
        elif i==']':
            begin=False
            ret_str.append(tmp_str)
        elif begin==True:
            tmp_str+=i
    return ret_str
def main():
    hands=get()
    eyes=get()
    mouths=get()

    collect=[len(hands),len(eyes),len(mouths),len(eyes),len(hands)]
    n=int(input())
    for i in range(n):
        my_str=input().split()
        prt=True
        for j in range(5):
            my_str[j]=int(my_str[j])-1
            if (my_str[j]>=collect[j] or my_str[j]<0):
                print('Are you kidding me? @\/@')
                prt=False
                break
        if prt==True:
            print(hands[my_str[0]],end='')
            print('(',end='')
            print(eyes[my_str[1]],end='')
            print(mouths[my_str[2]],end='')
            print(eyes[my_str[3]],end='')
            print(')',end='')
            print(hands[my_str[4]])
if __name__ == '__main__':
    main()
