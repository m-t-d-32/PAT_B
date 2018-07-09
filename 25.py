#PTA超时，牛客网通过。牛客网：https://www.nowcoder.com/questionTerminal/5f44c42fd21a42b8aeb889ab83b17ad0
def main():
    my_str=input().split()
    begin=int(my_str[0])
    n=int(my_str[1])
    k=int(my_str[2])

    raw_data=[None]*100005
    for i in range(n):
        my_str=input().split()
        my_pos=int(my_str[0])
        my_data=int(my_str[1])
        my_next=int(my_str[2])
        raw_data[my_pos]=(my_pos,my_data,my_next)
    i=begin
    tmp_results=[]
    while i!=-1:
        tmp_results.append(raw_data[i])
        i=raw_data[i][2]
    n=len(tmp_results)
    results=[]
    for i in range(0,n//k):
        begin=(i+1)*k
        end=i*k
        for j in range(begin-1,end-1,-1):
            results.append(tmp_results[j])
    for i in range(n//k*k,n):
        results.append(tmp_results[i])
    for i in range(n):
        if i!=n-1:
            print("%05d" % results[i][0]+' '+str(results[i][1])+' '+"%05d" % results[i+1][0])
        else:
            print("%05d" % results[i][0]+' '+str(results[i][1])+' -1')
if __name__ == '__main__':
    main()
