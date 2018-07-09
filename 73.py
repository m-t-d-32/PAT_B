def main():
    my_str=input().split()
    n=int(my_str[0])
    m=int(my_str[1])
    questions=[set() for i in range(m)]
    students=[0]*n
    scores=[0]*m
    errors=[dict() for i in range(m)]
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
            elif len(questions[j])>0 and len(ans-questions[j])==0:
                students[i]+=0.5*scores[j]
            tmp_set=(ans-questions[j]) | (questions[j]-ans)
            for t in tmp_set:
                if t not in errors[j]:
                    errors[j][t]=1
                else:
                    errors[j][t]+=1
    for i in range(n):
        print("%.1f" % students[i])

    max_error=0
    for i in range(m):
        my_list=list(errors[i].values())
        for j in my_list:
            if j>max_error:
                max_error=j
    if max_error==0:
        print('Too simple')
    else:
        for i in range(m):
            my_list=list(errors[i].keys())
            my_list.sort()
            for j in my_list:
                if errors[i][j]==max_error:
                    print(str(max_error)+' '+str(i+1)+'-'+j)

if __name__ == '__main__':
    main()
