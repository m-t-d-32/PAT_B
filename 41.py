class Student:
    def __init__(self,id,realnum):
        self.id=id
        self.realnum=realnum
    def print(self):
        print(self.id+" "+str(self.realnum))
def main():
    n=int(input())
    print(n)
    students=[None]*(n+5)
    for i in range(n):
        my_str=input().split()
        students[int(my_str[1])]=Student(my_str[0],my_str[2])
    m=int(input())
    searches=input().split()
    for i in range(len(searches)):
        students[int(searches[i])].print()
if __name__=='__main__':
    main()
