def main():
    str=input().split()
    begin=int(str[0])
    end=int(str[1])

    my_nums=[True]*110005
    for i in range(2,110000):
        if my_nums[i]==False:
            continue
        j=2
        while j*i<=110000:
            my_nums[i*j]=False
            j+=1
    my_results=[]
    for i in range(2,110000):
        if my_nums[i]:
            my_results.append(i)

    print_counter=0
    for i in range(begin-1,end):
        print(my_results[i],end='')
        print_counter+=1
        if print_counter==10 or i==end-1:
            print_counter=0
            print()
        else:
            print(' ',end='')
if __name__ == '__main__':
    main()
