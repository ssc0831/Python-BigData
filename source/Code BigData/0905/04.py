with open("C:/Users/admin/Desktop/Python, BigData/source/CSV/singer1.csv", "r") as inFp :
    with open("C:/Users/admin/Desktop/Python, BigData/source/CSV/new_singer3.csv", "w") as outFp:
        header = inFp.readline()
        header = header.strip()
        header_list = header.split(',')
        idx1 = header_list.index('아이디')
        idx2 = header_list.index('이름')
        idx3 = header_list.index('전화 번호')

        header_list = [header_list[idx1], header_list[idx2], header_list[idx3]]
        header_str = ','.join(map(str, header_list))
        outFp.write(header_str + '\n')
        
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            if row_list[idx3] != '':
                row_list = [row_list[idx2], row_list[idx1], row_list[idx3]]
                row_str = ','.join(map(str, row_list))
                outFp.write(row_str + '\n')

print('Save. OK~')
