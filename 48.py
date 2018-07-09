def main():
    my_str=input().split()
    str_a=my_str[0][::-1]
    str_b=my_str[1][::-1]
    result_str=''

    rep_char=('0','1','2','3','4','5','6','7','8','9','J','Q','K')
    rep_dict=dict()
    for i in range(len(rep_char)):
        rep_dict[rep_char[i]]=i

    if len(str_a)>len(str_b):
        str_b+='0'*(len(str_a)-len(str_b))
    else:
        str_a+='0'*(len(str_b)-len(str_a))
    for i in range(len(str_a)):
        temp_a=rep_dict[str_a[i]]
        temp_b=rep_dict[str_b[i]]
        if i & 1==0:
            temp_res=(temp_a+temp_b) % 13
        else:
            temp_res=(temp_b-temp_a)
            if temp_res<0:
                temp_res+=10
        result_str+=rep_char[temp_res]
    result_str=result_str[::-1]
    print(result_str)
if __name__ == '__main__':
    main()
