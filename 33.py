def lower(x):
    if x>='A' and x<='Z':
        return chr(ord(x)+ord('a')-ord('A'))
    else:
        return x
def main():
    bad_shift = False
    bad_input = input()
    bad_words = set()
    all_input = input()
    all_words = list()
    for i in all_input:
        all_words.append(lower(i))
    for i in bad_input:
        if i=='+':
            bad_shift=True
        else:
            bad_words.add(lower(i))
    for i in range(len(all_words)):
        if all_words[i] in bad_words:
            pass
        elif bad_shift and all_input[i]>='A' and all_input[i]<='Z':
            pass
        else:
            print(all_input[i],end='')
if __name__=='__main__':
    main()