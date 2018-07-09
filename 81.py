def main():
    n=int(input())
    for i in range(n):
        my_pwd=input()
        if len(my_pwd)<6:
            print('Your password is tai duan le.')
        else:
            has_Letter=False
            has_Number=False
            has_Else=False
            for i in my_pwd:
                if i>='0' and i<='9':
                    has_Number=True
                elif i>='A' and i<='Z' or i>='a' and i<='z':
                    has_Letter=True
                elif i!='.':
                    has_Else=True
            if has_Else:
                print('Your password is tai luan le.')
            elif not has_Number:
                print('Your password needs shu zi.')
            elif not has_Letter:
                print('Your password needs zi mu.')
            else:
                print('Your password is wan mei.')
if __name__ == '__main__':
    main()
