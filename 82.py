def main():
    low_number=None
    low_score=0
    high_number=None
    high_score=20005
    n=int(input())
    for i in range(n):
        my_str=input().split()
        x=int(my_str[1])
        y=int(my_str[2])
        score=x*x+y*y
        if score<high_score:
            high_score=score
            high_number=my_str[0]
        if score>low_score:
            low_score=score
            low_number=my_str[0]
    print(high_number+' '+low_number)
if __name__ == '__main__':
    main()
