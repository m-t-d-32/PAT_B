def main():
    my_str=input().split()
    n=int(my_str[0])
    elec_down=float(my_str[1])
    elec_day=int(my_str[2])
    
    elec_doubt=0
    elec_true=0
    for i in range(n):
        my_str=input().split()
        m=int(my_str[0])
        count=0
        for j in range(1,m+1):
            if float(my_str[j])<elec_down:
                count+=1
        if count*2>m:
            if m>elec_day:
                elec_true+=1
            else:
                elec_doubt+=1
    doubt=100*elec_doubt/n
    true=100*elec_true/n
    print("%.1f%% %.1f%%" % (doubt,true))
if __name__=='__main__':
    main()