def main():
    My_str=input()
    Chn_str=['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
    sum=0
    for i in My_str:
        sum+=ord(i)-ord('0')

    My_sum=str(sum)
    for i in range(len(My_sum)-1):
        print(Chn_str[ord(My_sum[i])-ord('0')],end=' ')
    print(Chn_str[ord(My_sum[len(My_sum)-1])-ord('0')])

if __name__ == '__main__':
    main()
