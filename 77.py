def main():
    my_str=input().split()
    n=int(my_str[0])
    m=int(my_str[1])
    for i in range(n):
        sum=0
        my_str=input().split()
        my_scores=[]
        for j in range(1,n):
            score=int(my_str[j])
            if score>=0 and score<=m:
                my_scores.append(score)
        my_scores.sort()
        count=len(my_scores)
        for j in range(1,count-1):
            sum+=my_scores[j]
        avg=(sum/(count-2)+int(my_str[0]))/2
        print(int(avg+0.5))
if __name__ == '__main__':
    main()
