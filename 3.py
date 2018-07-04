def check(str):
    p=0
    t=0
    other=0
    for i in str:
        if i=='P':
            p+=1
        elif i=='T':
            t+=1
        elif i!='A':
            other+=1

    if p==1 and t==1 and other==0 and str.find('P')<str.find('T'):
        return True
    else:
        return False
def clean_chk(str):
    p_pos=str.find('P')
    t_pos=str.find('T')

    a1=p_pos
    a2=t_pos-p_pos-1
    a3=len(str)-t_pos-1

    if a1==0 and a3==0 and a2>0:
        return True
    while a3>a1 and a2>0:
        a2-=1
        a3-=a1

    if a3==a1 and a2==1:
        return True
    else:
        return False
def main():
    n=int(input())

    for i in range(n):
        My_str=input()
        if check(My_str):
            if clean_chk(My_str):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
if __name__ == '__main__':
    main()
