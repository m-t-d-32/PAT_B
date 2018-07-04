def main():
    my_num=input()
    every_num=[0]*10
    for i in my_num:
        every_num[ord(i)-ord('0')]+=1
    for i in range(len(every_num)):
        if every_num[i]!=0:
            print(str(i)+":"+str(every_num[i]))
if __name__ == '__main__':
    main()
