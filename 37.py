def main():
    my_str=input().split()
    P=my_str[0].split('.')
    A=my_str[1].split('.')

    real_P=int(P[0])*17*29+int(P[1])*29+int(P[2])
    real_A=int(A[0])*17*29+int(A[1])*29+int(A[2])
    remain=real_A-real_P

    if remain<0:
        print('-',end='')
        remain=-remain
    kunt=remain%29
    remain//=29
    sickle=remain%17
    gallon=remain//17

    print(str(gallon)+'.'+str(sickle)+'.'+str(kunt))
if __name__ == '__main__':
    main()
