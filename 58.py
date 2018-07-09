def main():
    my_str=input().split()
    n=int(my_str[0])
    m=int(my_str[1])
    questions=[set() for i in range(m)]
    students=[0]*n
    scores=[0]*m
    errors=[0]*m
    for i in range(m):
        my_str=input().split()
        scores[i]=int(my_str[0])
        for j in range(3,len(my_str)):
            questions[i].add(my_str[j])
    for i in range(n):
        my_str=input().split(')')
        for j in range(m):
            sel_str=my_str[j].split()
            ans=set()
            for t in range(1,len(sel_str)):
                ans.add(sel_str[t][0])
            if ans==questions[j]:
                students[i]+=scores[j]
            else:
                errors[j]+=1
    for i in range(n):
        print(students[i])

    max_error=0
    for i in range(m):
        if errors[i]>max_error:
            max_error=errors[i]
    if max_error==0:
        print('Too simple')
    else:
        print(max_error,end='')
        for i in range(m):
            if errors[i]==max_error:
                print(' '+str(i+1),end='')
if __name__ == '__main__':
    main()
