def main():
    my_str=input()
    my_p=my_pa=my_pat=0
    for i in my_str:
        if i=='P':
            my_p+=1
        elif i=='A':
            my_pa+=my_p
        elif i=='T':
            my_pat+=my_pa
    print(my_pat%1000000007)
if __name__ == '__main__':
    main()
