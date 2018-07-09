import math
def main():
    n=int(input())
    my_str=input().split()
    for i in range(n):
        my_str[i]=int(my_str[i])
    my_str.sort(reverse=True)
    x=int(math.sqrt(n))
    y=math.ceil(math.sqrt(n))
    while x*y!=n:
        if x*y<n:
            y+=1
        else:
            x-=1
    my_array=[[0 for i in range(x)] for j in range(y)]

    walk_x=1    #现在的方向
    walk_y=0
    now_x=0     #现在的位置
    now_y=0
    all_x=x     #现在的方向最大行进的长度
    all_y=y-1
    used_x=0    #现在的方向这次行进的长度
    used_y=0

    for i in my_str:
        my_array[now_y][now_x]=i
        if walk_x!=0:
            used_x+=1
        else:
            used_y+=1

        if walk_x==1 and used_x==all_x:
            walk_x=0
            walk_y=1
            all_x-=1
            used_x=0
        elif walk_y==1 and used_y==all_y:
            walk_x=-1
            walk_y=0
            all_y-=1
            used_y=0
        elif walk_x==-1 and used_x==all_x:
            walk_x=0
            walk_y=-1
            all_x-=1
            used_x=0
        elif walk_y==-1 and used_y==all_y:
            walk_x=1
            walk_y=0
            all_y-=1
            used_y=0

        now_x+=walk_x
        now_y+=walk_y
    for i in range(y):
        for j in range(x-1):
            print(my_array[i][j],end=' ')
        print(my_array[i][x-1])

if __name__=='__main__':
    main()
