#PTA超时，牛客网能过。牛客网：https://www.nowcoder.com/questionTerminal/79db907555c24b15a9c73f7f7d0e2471
def main():
    n=int(input())
    #reference CA,JA,BA,CB,JB,BB
    names='BCJBCJ'  # use these to win
    selects=[0,0,0,2,2,2] # for A:win--0 lose--2
    gets=['B C','C J','J B','C B','J C','B J']
    results=[0]*3 #for A
    wins=[0]*6
    for i in range(n):
        my_str=input()
        if my_str[0]==my_str[2]:
            results[1]+=1
            continue
        for j in range(6):  #len(gets)
            if gets[j]==my_str:
                wins[j]+=1
                results[selects[j]]+=1
                break
    print(str(results[0])+" "+str(results[1])+" "+str(results[2]))
    print(str(results[2])+" "+str(results[1])+" "+str(results[0]))

    A=B=0
    maxA=maxB=0
    for i in range(0,3):
        if wins[i]>maxA:
            A=i
            maxA=wins[i]
    for i in range(3,6):
        if wins[i]>maxB:
            B=i
            maxB=wins[i]
    print(str(names[A])+" "+str(names[B]))
if __name__ == '__main__':
    main()
