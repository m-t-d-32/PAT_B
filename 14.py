def min(a,b):
    if a<b:
        return len(a)
    else:
        return len(b)
def isCapitalLetter(a):
    if a>='A' and a<='G':
        return True
    else:
        return False
def isLetter(a):
    if a>='A' and a<='Z' or a>='a' and a<='z':
        return True
    else:
        return False
def isSyn(a):
    if a>='A' and a<='N' or a>='0' and a<='9':
        return True
    else:
        return False

def main():
    str1=input()
    str2=input()
    str3=input()
    str4=input()
    WeekDay=['MON','TUE','WED','THU','FRI','SAT','SUN']
    isSecond=False
    for i in range(min(str1,str2)):
        if str1[i]==str2[i] and isCapitalLetter(str1[i]) and isSecond==False:
            isSecond=True
            print(WeekDay[ord(str1[i])-ord('A')],end=' ')
        elif str1[i]==str2[i] and isSyn(str1[i]) and isSecond==True:
            if ord(str1[i])<=ord('9'):
                print('0'+str1[i],end=':')
            else:
                print(int(ord(str1[i])-ord('A')+10),end=':')
            break
    for i in range(min(str3,str4)):
        if str3[i]==str4[i] and isLetter(str3[i]):
            print('%02d' % i)
            break
if __name__ == '__main__':
    main()
