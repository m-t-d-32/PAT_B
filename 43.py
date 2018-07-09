def main():
    my_str=input()
    char_const='PATest'
    char_array=[0]*6 #for 'PATest'
    for i in my_str:
        for j in range(len(char_const)):
            if char_const[j]==i:
                char_array[j]+=1
    while True:
        keyed=False
        for i in range(len(char_array)):
            if char_array[i]!=0:
                print(char_const[i],end='')
                char_array[i]-=1
                keyed=True
        if keyed==False:
            break
if __name__ == '__main__':
    main()
