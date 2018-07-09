def main():
    n=int(input())
    for i in range(n):
        my_str=input()
        right_ans=my_str[my_str.find('T')-2]
        right_num=ord(right_ans)-ord('A')+1
        print(right_num,end='')
if __name__ == '__main__':
    main()
