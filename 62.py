def chk(x,y):
    if x>y:
        x,y=y,x
    while y%x!=0:
        x,y=y%x,x
    if x==1:
        return True
    else:
        return False
def main():
    my_str=input().split()
    frac1=my_str[0].split('/')
    frac1_i=int(frac1[0])
    frac1_d=int(frac1[1])
    frac2=my_str[1].split('/')
    frac2_i=int(frac2[0])
    frac2_d=int(frac2[1])
    common_d=int(my_str[2])

    if frac1_i*frac2_d>frac1_d*frac2_i:
        frac1_i,frac2_i=frac2_i,frac1_i
        frac1_d,frac2_d=frac2_d,frac1_d
    results=[]
    my_begin=0
    while my_begin*frac1_d<=frac1_i*common_d:
        my_begin+=1
    while my_begin*frac2_d<frac2_i*common_d:
        if chk(my_begin,common_d):
            results.append(my_begin)
        my_begin+=1
    for i in range(len(results)-1):
        print(str(results[i])+'/'+str(common_d),end=' ')
    print(str(results[len(results)-1])+'/'+str(common_d))
if __name__ == '__main__':
    main()
