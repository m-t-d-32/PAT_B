def main():
    my_nums=[False,False]
    n=int(input())
    sum=0
    for i in range(2,n+1):
        my_nums.append(True)
    for i in range(2,n+1):
        if my_nums[i]==False:
            continue
        j=2
        while j*i<=n:
            my_nums[j*i]=False
            j+=1
    my_primes=[]
    for i in range(2,n+1):
        if my_nums[i]==True:
            my_primes.append(i)
    for i in range(len(my_primes)-1):
        if my_primes[i+1]-my_primes[i]==2:
            sum+=1
    print(sum)

if __name__ == '__main__':
    main()
