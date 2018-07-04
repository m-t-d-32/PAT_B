class Student:
    def __init__(self,name,num,score):
        self.name=name
        self.num=num
        self.score=score
def takeSecond(l):
    return l.score

def main():
    n=int(input())
    students=[]
    for i in range(n):
        strs=input().split(' ')
        students.append(Student(strs[0],strs[1],int(strs[2])))
    students.sort(key=takeSecond)

    print(students[len(students)-1].name+" "+students[len(students)-1].num)
    print(students[0].name+" "+students[0].num)
if __name__ == '__main__':
    main()
