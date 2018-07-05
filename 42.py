def main():
    my_str=input()
    word_freq=[0]*26
    for i in my_str:
        if i>='A' and i<='Z':
            word_freq[ord(i)-ord('A')]+=1
        elif i>='a' and i<='z':
            word_freq[ord(i)-ord('a')]+=1
    max_index=0
    max_num=0
    for i in range(26):
        if word_freq[i]>max_num:
            max_num=word_freq[i]
            max_index=i
    print(chr(max_index+ord('a'))+' '+str(max_num))
if __name__ == '__main__':
    main()
