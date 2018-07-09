def main():
    my_str=input().split()
    y=int(my_str[0])
    x=int(my_str[1])
    tol=int(my_str[2])

    picture=[[0 for j in range(y)] for i in range(x)]
    my_set=dict()
    for i in range(x):
        my_str=input().split()
        for j in range(y):
            picture[i][j]=int(my_str[j])
            if picture[i][j] in my_set:
                my_set[picture[i][j]]+=1
            else:
                my_set[picture[i][j]]=1
    besides=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    uniques=None
    count=0
    for i in range(x):
        for j in range(y):
            unique=True
            if my_set[picture[i][j]]>1:
                continue
            for t in range(8):
                tx=besides[t][0]+i
                ty=besides[t][1]+j
                if tx>=0 and ty>=0 and tx<x and ty<y and abs(picture[i][j]-picture[tx][ty])<=tol:
                    unique=False
                    break
            if unique==True:
                uniques=(i,j)
                count+=1
    if count==0:
        print('Not Exist')
    elif count>1:
        print('Not Unique')
    else:
        rx=uniques[0]
        ry=uniques[1]
        print('('+str(ry+1)+', '+str(rx+1)+'): '+str(picture[rx][ry]))
if __name__ == '__main__':
    main()
