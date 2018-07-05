def main():
    all_str=list(input())
    my_str=list(input())
    all_str.sort()
    my_str.sort()
    i=j=0
    distance=0
    while i<len(all_str) and j<len(my_str):
        if all_str[i]<my_str[j]:
            i+=1
        elif all_str[i]==my_str[j]:
            i+=1
            j+=1
        else:
            distance+=1
            j+=1
    if distance==0 and j==len(my_str):
        print('Yes '+str(len(all_str)-len(my_str)))
    else:
        print('No '+str(distance+len(my_str)-j))
if __name__ == '__main__':
    main()
