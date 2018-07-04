def main():
    my_dict=dict()
    n=int(input())
    my_num=input().split()
    for i in range(n):
        my_dict[int(my_num[i])]=False
    for i in range(n):
        key=int(my_num[i])
        if my_dict[key]==True:
            continue
        while key>1:
            if key % 2==1:
                key=3*key+1
                key=key/2
            else:
                key=key/2
            if key in my_dict:
                my_dict[key]=True
    results=[]
    for (d,x) in my_dict.items():
        if x==False:
            results.append(d)
    results.sort(reverse=True)
    for i in range(len(results)-1):
        print(results[i],end=' ')
    if (len(results)>0):
        print(results[len(results)-1])
if __name__ == '__main__':
    main()
