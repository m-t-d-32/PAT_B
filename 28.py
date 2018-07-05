#PAT超时，牛客网过了，牛客网：https://www.nowcoder.com/questionTerminal/77b981c8312f47b7b59795c3b173d326
def main():
    my_num=int(input())
    today=2014*360+9*30+6
    min_time=99999999
    min_name=''
    max_time=0
    max_name=''
    count=0
    for i in range(my_num):
        my_input=input().split()
        my_name=my_input[0]
        my_str=my_input[1].split('/')
        yy=int(my_str[0])
        mm=int(my_str[1])
        dd=int(my_str[2])

        chk_day=yy*360+mm*30+dd
        if chk_day>today or chk_day+200*360<today:
            continue
        else:
            count+=1
            if chk_day>max_time:
                max_name=my_name
                max_time=chk_day
            if chk_day<min_time:
                min_name=my_name
                min_time=chk_day
    if count==0:
        print(0)
    else:
        print(str(count)+' '+min_name+' '+max_name)
if __name__ == '__main__':
    main()
