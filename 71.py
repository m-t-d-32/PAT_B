def main():
    my_str=input().split()
    money=int(my_str[0])
    n=int(my_str[1])
    for i in range(n):
        if money==0:
            print('Game Over.')
            break
        my_str=input().split()
        n1=int(my_str[0])
        guess=int(my_str[1])
        play_money=int(my_str[2])
        n2=int(my_str[3])

        if play_money>money:
            print('Not enough tokens.  Total = '+str(money)+'.')
            continue
        if (n1<n2) ^ guess:
            money-=play_money
            print('Lose '+str(play_money)+'.  Total = '+str(money)+'.')
        else:
            money+=play_money
            print('Win '+str(play_money)+'!  Total = '+str(money)+'.')
if __name__ == '__main__':
    main()
