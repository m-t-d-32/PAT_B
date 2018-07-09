def main():
    n=int(input())
    sum=0
    count=0
    my_str=input().split()
    for i in range(n):
        try:
            if my_str[i].find('.')!=-1 and my_str[i].find('.')+3<len(my_str[i]):
                raise TypeError
            key=float(my_str[i])
            if key<=1000 and key>=-1000:
                sum+=key
                count+=1
            else:
                raise TypeError
        except:
            print('ERROR: '+my_str[i]+' is not a legal number')
    if count==0:
        print('The average of 0 numbers is Undefined')
    elif count==1:
        print('The average of 1 number is '+"%.2f" % (sum/count))
    else:
        print('The average of '+str(count)+' numbers is '+"%.2f" % (sum/count))
if __name__=='__main__':
    main()