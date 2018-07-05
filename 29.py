def upper(i):
    if i>=ord('a') and i<=ord('z'):
        return i+ord('A')-ord('a')
    else:
        return i
def main():
    my_str=input()
    key_str=input()

    my_chars=[False]*128
    for i in my_str:
        my_chars[upper(ord(i))]=True
    for i in key_str:
        my_chars[upper(ord(i))]=False
    for i in my_str:
        if my_chars[upper(ord(i))]:
            print(chr(upper(ord(i))),end='')
            my_chars[upper(ord(i))]=False
if __name__ == '__main__':
    main()
