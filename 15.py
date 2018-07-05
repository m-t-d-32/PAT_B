#PTA超时，牛客网过了。牛客网：https://www.nowcoder.com/questionTerminal/97b6a49a85944650b2e3d0660b91c324
class Student:
    def __init__(self,number,D_score,C_score):
        self.number=number
        self.D_score=D_score
        self.C_score=C_score
        self.W_score=D_score+C_score

def get_key(stu):
    return -stu.W_score,-stu.D_score,stu.number
def main():
    my_str=input().split()
    sum=int(my_str[0])
    low=int(my_str[1])
    high=int(my_str[2])

    my_students=[[],[],[],[]]
    result_sum=0
    for i in range(sum):
        tmp_str=input().split()
        tmp_num=int(tmp_str[0])
        tmp_D=int(tmp_str[1])
        tmp_C=int(tmp_str[2])
        tmp_stu=Student(tmp_num,tmp_D,tmp_C)

        if tmp_stu.D_score>=low and tmp_stu.C_score>=low:
            if tmp_stu.D_score>=high and tmp_stu.C_score>=high:
                my_students[0].append(tmp_stu)
            elif tmp_stu.D_score>=high:
                my_students[1].append(tmp_stu)
            elif tmp_stu.D_score>=tmp_stu.C_score:
                my_students[2].append(tmp_stu)
            else:
                my_students[3].append(tmp_stu)
            result_sum+=1
    for i in range(4):
        my_students[i].sort(key=get_key)
    print(result_sum)
    for i in range(4):
        for j in my_students[i]:
            print(str(j.number)+' '+str(j.D_score)+' '+str(j.C_score))

if __name__=='__main__':
    main()
