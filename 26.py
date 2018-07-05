def main():
    my_str=input().split()
    my_time=int(my_str[1])-int(my_str[0])
    my_time=int(my_time/100+0.5)

    hh=my_time//3600
    my_time%=3600
    mm=my_time//60
    my_time%=60
    ss=my_time
    print("%02d" % hh+':'+"%02d" % mm+':'+"%02d" % ss)
if __name__ == '__main__':
    main()
