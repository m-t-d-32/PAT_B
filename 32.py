#PTA超时，牛客网通过。牛客网：https://www.nowcoder.com/questionTerminal/8ec60eb06fad461eb82ff30562eedc31
def main():
    n=int(input())
    my_schools=[0]*100005
    for i in range(n):
        my_str=input().split()
        my_schools[int(my_str[0])]+=int(my_str[1])
    max_num=0
    max_value=0
    for i in range(100005):
        if my_schools[i]>max_value:
            max_value=my_schools[i]
            max_num=i
    print(str(max_num)+' '+str(max_value))
if __name__ == '__main__':
    main()
