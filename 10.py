def main():
    My_str=input().split()
    i=0
    My_result=[]
    while i<len(My_str):
        a=int(My_str[i])
        i+=1
        b=int(My_str[i])
        i+=1

        if b!=0:
            My_result.append(a*b)
            My_result.append(b-1)

    if len(My_result)==0:
        print('0 0')
    else:
        for i in range(len(My_result)-1):
            print(My_result[i],end=' ')
        print(My_result[len(My_result)-1])
if __name__ == '__main__':
    main()
