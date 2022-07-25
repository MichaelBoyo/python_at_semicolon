def timeConversion(s):
    if s[-2] + s[-1] in 'PMpm' and int(s[0]+s[1]) <12 :
        str_ = str(int(s[0]+s[1])+12)
        return str_+s[2:-2]
    elif int(s[0]+s[1]) == 12:
        return '00'+s[2:-1]
    else:
        return s[:-2]


print(timeConversion("07:05:45PM"))