def judge_equal(my_str,result):
    if len(my_str)!=len(result):
        return False
    for i in range(len(my_str)):
        if my_str[i]!=result[i]:
            return False
    return True
def my_print(my_str):
    for i in range(len(my_str)-1):
        print(my_str[i],end=' ')
    print(my_str[len(my_str)-1])
def link(my_str,begin,middle,end):
    my_temp=[0]*len(my_str)
    tmp_idx=begin
    l_begin=begin
    l_end=middle
    r_begin=middle
    r_end=end
    while l_begin<l_end and r_begin<r_end:
        if my_str[l_begin]<my_str[r_begin]:
            my_temp[tmp_idx]=my_str[l_begin]
            l_begin+=1
        else:
            my_temp[tmp_idx]=my_str[r_begin]
            r_begin+=1
        tmp_idx+=1
    while l_begin<l_end:
        my_temp[tmp_idx]=my_str[l_begin]
        l_begin+=1
        tmp_idx+=1
    while r_begin<r_end:
        my_temp[tmp_idx]=my_str[r_begin]
        r_begin+=1
        tmp_idx+=1
    for i in range(begin,end):
        my_str[i]=my_temp[i]
    return my_str
def judge_merge(my_str,result):
    step=1
    my_break=False
    while step<len(my_str):
        i=0
        while i+step<len(my_str):
            if i+2*step<len(my_str):
                my_str=link(my_str,i,i+step,i+2*step)
            else:
                my_str=link(my_str,i,i+step,len(my_str))
            i+=2*step
        if my_break==True:
            my_print(my_str)
            return
        if judge_equal(my_str,result):
            print('Merge Sort')
            my_break=True
        step*=2
def judge_insert(my_str,result):
    my_break=False
    for i in range(1,len(my_str)):
        for j in range(i):
            if my_str[j]>my_str[i]:
                tmp=my_str[i]
                for t in range(i,j,-1):
                    my_str[t]=my_str[t-1]
                my_str[j]=tmp
        if my_break==True:
            my_print(my_str)
            return
        if judge_equal(my_str,result):
            print('Insertion Sort')
            my_break=True
def main():
    n=int(input())
    my_str=input().split()
    results=input().split()
    str1=[]
    str2=[]
    for i in range(len(my_str)):
        str1.append(int(my_str[i]))
        str2.append(str1[i])
        results[i]=int(results[i])
    judge_insert(str1,results)
    judge_merge(str2,results)
if __name__ == '__main__':
    main()
