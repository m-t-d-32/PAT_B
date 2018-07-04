'''
def main():
    my_str=input().split()
    divided=int(my_str[0])
    divide=int(my_str[1])
    print(str(divided//divide)+" "+str(divided%divide))
if __name__ == '__main__':
    main()
'''

def main():
    my_str=input().split()
    divided=my_str[0]
    divide=int(my_str[1])

    remain=0
    result=''
    for i in divided:
        tmp=remain*10+ord(i)-ord('0')
        result+=str(int(tmp)//divide)
        remain=int(tmp)%divide
    if result[0]=='0' and len(result)>1:
        result=result[1:]
    print(result+" "+str(remain))
if __name__ == '__main__':
    main()
