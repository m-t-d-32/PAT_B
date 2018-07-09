def gcd(x,y):
    bkx=x
    bky=y
    while y%x!=0:
        x,y=y%x,x
    return bkx//x,bky//x
def conv(x,y):
    if x<0:
        x=-x
        y=-y
    elif x==0:
        return '0'
    neg=False
    if y<0:
        neg=True
        y=-y
    elif y==0:
        return 'Inf'

    rtn=''
    if x>=y:
        rtn=str(x//y)
        x%=y
        if x==0:
            if neg:
                return '(-'+rtn+')'
            else:
                return rtn
        else:
            rtn+=' '
    x,y=gcd(x,y)
    rtn+=str(x)+'/'+str(y)
    if neg:
        return '(-'+rtn+')'
    else:
        return rtn

def main():
    my_str=input().split()
    v_a=my_str[0].split('/')
    v_b=my_str[1].split('/')

    frac1_i=int(v_a[0])
    frac1_d=int(v_a[1])
    frac2_i=int(v_b[0])
    frac2_d=int(v_b[1])

    add_result_i=frac1_i*frac2_d+frac2_i*frac1_d
    add_result_d=frac1_d*frac2_d
    sub_result_i=frac1_i*frac2_d-frac2_i*frac1_d
    sub_result_d=frac1_d*frac2_d
    mul_result_i=frac1_i*frac2_i
    mul_result_d=frac1_d*frac2_d
    div_result_i=frac1_i*frac2_d
    div_result_d=frac2_i*frac1_d

    print(conv(frac1_i,frac1_d)+' + '+conv(frac2_i,frac2_d)+' = '+conv(add_result_i,add_result_d))
    print(conv(frac1_i,frac1_d)+' - '+conv(frac2_i,frac2_d)+' = '+conv(sub_result_i,sub_result_d))
    print(conv(frac1_i,frac1_d)+' * '+conv(frac2_i,frac2_d)+' = '+conv(mul_result_i,mul_result_d))
    print(conv(frac1_i,frac1_d)+' / '+conv(frac2_i,frac2_d)+' = '+conv(div_result_i,div_result_d))
if __name__ == '__main__':
    main()
