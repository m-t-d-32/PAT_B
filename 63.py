import math
def main():
    n=int(input())
    max_result=0
    for i in range(n):
        my_str=input().split()
        real=int(my_str[0])
        imag=int(my_str[1])
        if math.sqrt(real*real+imag*imag)>max_result:
            max_result=math.sqrt(real*real+imag*imag)
    print("%.2f" % max_result)
if __name__ == '__main__':
    main()
