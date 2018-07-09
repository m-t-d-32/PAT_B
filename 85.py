class School:
    def __init__(self,name,score):
        self.name=name
        self.score=score
        self.count=1
    def add(self,score):
        self.score+=score
        self.count+=1
    def print(self,rank):
        print(str(rank)+' '+self.name+' '+str(self.score)+' '+str(self.count))
def get_key(school):
    return -school.score,school.count,school.name
def main():
    n=int(input())
    my_schools=dict()
    for i in range(n):
        my_str=input().split()
        school=my_str[2].lower()
        score=int(my_str[1])
        if my_str[0][0]=='B':
            score/=1.5
        elif my_str[0][0]=='T':
            score*=1.5
        score=int(score)
        if school not in my_schools:
            my_schools[school]=School(school,score)
        else:
            my_schools[school].add(score)
    results=list(my_schools.values())
    results.sort(key=get_key)
    print(len(results))
    results[0].print(1)
    rank=1
    for i in range(1,len(results)):
        if results[i].score!=results[i-1].score:
            rank=i+1
        results[i].print(rank)
if __name__ == '__main__':
    main()
