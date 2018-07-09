def main():
    my_str=input().split()
    n=int(my_str[0])
    m=int(my_str[1])
    scores=[0]*m
    right_ans=[0]*m
    my_str=input().split()
    for i in range(m):
        scores[i]=int(my_str[i])
    my_str=input().split()
    for i in range(m):
        right_ans[i]=int(my_str[i])
    for i in range(n):
        my_str=input().split()
        sum=0
        for j in range(m):
            if int(my_str[j])==right_ans[j]:
                sum+=scores[j]
        print(sum)
if __name__ == '__main__':
    main()
