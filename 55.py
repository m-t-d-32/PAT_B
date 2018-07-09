class Student:
    def __init__(self,name,height):
        self.name=name
        self.height=height
def get_key(student):
    return -student.height,student.name
def main():
    my_str=input().split()
    n=int(my_str[0])
    m=int(my_str[1])
    students=[]
    every_line=n//m
    for i in range(n):
        my_str=input().split()
        students.append(Student(my_str[0],int(my_str[1])))
    students.sort(key=get_key,reverse=True)
    results=[]
    for i in range(m):
        begin=every_line*i
        if i!=m-1:
            end=begin+every_line
        else:
            end=n
        tmp_result=[0]*(end-begin)
        middle=(begin+end)//2
        my_symbol=1
        my_state=0
        for j in range(end-1,begin-1,-1):
            tmp_result[middle+my_symbol*my_state-begin]=students[j].name
            if my_symbol==1:
                my_state+=1
            my_symbol=-my_symbol
        results.append(tmp_result)
    for i in range(len(results)-1,-1,-1):
        print(' '.join(results[i]))
if __name__ == '__main__':
    main()
