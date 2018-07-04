def main():
    my_str=input().split()
    add_a=int(my_str[0])
    add_b=int(my_str[1])
    result_radix=int(my_str[2])

    add_result=add_a+add_b
    results=[]
    while add_result>0:
        results.append(add_result%result_radix)
        add_result=add_result//result_radix
    if len(results)==0:
        print(0)
    while len(results)>0:
        print(results.pop(),end='')
if __name__ == '__main__':
    main()
