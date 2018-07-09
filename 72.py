def main():
    my_str=input().split()
    n=int(my_str[0])
    m=int(my_str[1])
    deletes=set()
    my_str=input().split()
    all_stu=0
    all_problem=0
    for i in range(m):
        deletes.add(my_str[i])
    for i in range(n):
        my_str=input().split()
        name=my_str[0]
        problems=[]
        num=int(my_str[1])
        for j in range(num):
            if my_str[j+2] in deletes:
                problems.append(my_str[j+2])
        if len(problems)!=0:
            all_stu+=1
            print(name+':',end='')
            for j in range(len(problems)):
                print(' '+problems[j],end='')
                all_problem+=1
            print()
    print(str(all_stu)+' '+str(all_problem))
if __name__ == '__main__':
    main()
