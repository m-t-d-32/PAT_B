def chk_num(my_str):
    for i in range(len(my_str)-1):
        if my_str[i]!=my_str[i+1]:
            return True
    return False
def main():
    n=input()
    n="%04d" % (int(n))
    if chk_num(n):
        while True:
            my_list=list(n)
            maxL=''.join(sorted(my_list,reverse=True))
            minL=''.join(sorted(my_list,reverse=False))
            n="%04d" % (int(maxL)-int(minL))
            print(maxL+" - "+minL+" = "+n)
            if n=='6174':
                break
    else:
        print(n+" - "+n+" = 0000")
if __name__ == '__main__':
    main()
