CHRS_L = ['tret', 'jan', 'feb', 'mar',
          'apr', 'may', 'jun', 'jly',
          'aug', 'sep', 'oct', 'nov', 'dec']
CHRS_H = ['tret','tam', 'hel', 'maa', 'huh',
          'tou', 'kes', 'hei', 'elo', 'syy',
          'lok', 'mer', 'jou']
def prt_char(my_int):
    low = my_int % 13
    high = my_int // 13
    if high == 0:
        print(CHRS_L[low])
    elif low == 0:
        print(CHRS_H[high])
    else:
        print(CHRS_H[high]+' '+CHRS_L[low])
def prt_int(my_str):
    l_str=my_str.split()
    if len(l_str)==1:
        for i in range(len(CHRS_H)):
            if CHRS_H[i]==l_str[0]:
                print(i*13)
                return
        for i in range(len(CHRS_L)):
            if CHRS_L[i]==l_str[0]:
                print(i)
                return
    else:
        sum=0
        for i in range(len(CHRS_H)):
            if CHRS_H[i]==l_str[0]:
                sum+=i*13
                break
        for i in range(len(CHRS_L)):
            if CHRS_L[i]==l_str[1]:
                sum+=i
                break
        print(sum)
def main():
    n = int(input())
    for i in range(n):
        my_str = input()
        if my_str[0] >= '0' and my_str[0] <= '9':
            prt_char(int(my_str))
        else:
            prt_int(my_str)
if __name__ == '__main__':
    main()
