data = '16 03 01 02 00 01 00 01 fc 03 03 21 3f b1 77 e1'


def Escape_data():
    new_data = data.replace(' ','') # 去除空格
    datalenth = len(new_data)
    result = ''
    for x in range(0,datalenth):
        team = new_data[x:x+2]
        if team == '00' or team == '22':
            result += rf'\\x{team}'
        else:
            result += rf'\x{team}'
    return result

def main():
    print(Escape_data())


if __name__ == '__main__':
    main()