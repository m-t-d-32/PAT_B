def main():
    my_input=int(input())
    sum=0
    while my_input>1:
        if my_input%2==0:
            my_input/=2
            sum+=1
        else:
            my_input=my_input*3+1
    print(sum)

if __name__ == '__main__':
    main()
