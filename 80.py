class Student:
    def __init__(self):
        self.name=None
        self.gp=-1
        self.gm=-1
        self.gf=-1

students=dict()

def readin():
    my_str=input().split()
    name=my_str[0]
    score=int(my_str[1])
    if name not in students:
        students[name]=Student()
        students[name].name=name
    return name,score
def get_key(student):
    return -get_grade(student),student.name
def get_grade(student):
    if student.gf>student.gm:
        all_grade=student.gf
    else:
        all_grade=0.4*student.gm+0.6*student.gf
    return int(all_grade+0.5)
def main():
    my_str=input().split()
    p=int(my_str[0])
    m=int(my_str[1])
    n=int(my_str[2])

    for i in range(p):
        name,score=readin()
        students[name].gp=score
    for i in range(m):
        name,score=readin()
        students[name].gm=score
    for i in range(n):
        name,score=readin()
        students[name].gf=score
    results=[]
    for i in students:
        student=students[i]
        if student.gp<200:
            continue
        else:
            all_grade=get_grade(student)
            if all_grade>=60:
                results.append(student)
    results.sort(key=get_key)
    for student in results:
        print(student.name+' '+str(student.gp)+' '+str(student.gm)+' '+str(student.gf)+' '+str(get_grade(student)))
if __name__ == '__main__':
    main()
