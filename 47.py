def main():
    n=int(input())
    my_teams=[0]*1005
    for i in range(n):
        my_str=input().split()
        my_team=my_str[0].split('-')
        my_teams[int(my_team[0])]+=int(my_str[1])
    max_team=-1
    max_score=0
    for i in range(1005):
        if my_teams[i]>max_score:
            max_score=my_teams[i]
            max_team=i

    print(str(max_team)+' '+str(max_score))
if __name__ == '__main__':
    main()        
