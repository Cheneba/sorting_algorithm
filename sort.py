

def compare(data, data1, data2, passcode, start=0, end=0):
    space1 = data.index(data1)
    space2 = data.index(data2)
    print(space1, space2)
    if passcode=='int':
        if data1>data2:
            data[space1], data[space2] = data[space2], data[space1]

    elif passcode == 'alnum':   
        count1 = 0
        count2 = 0
        for index in range(start, end):
            if isinstance(data1[index], int):
                count1+=1
        for index2 in range(index, end):
            if isinstance(data2[index2], int):
                count2+=1
        if count1>count2:
            data[space1], data[space2] = data[space2], data[space1]
        elif count1==count2:
            newList1 = data1[:count1]
            newList2 = data1[:count2]
            if newList1>newList2:
                data[space1], data[space2] = data[space2], data[space1]


    elif passcode=='str':
        if len(data1)>len(data2):
            lowerlen = len(data2)
        else: lowerlen = len(data1)
        for x in range(lowerlen):
            if(ord(data1[x]) > ord(data2[x])):
                data[space1], data[space2] = data[space2], data[space1]
                break
            


def sortNum(data):
    count = 0
    for i in range(len(data)):
        if isinstance(data[i], int):
            x = data[i]
            data.remove(data[i])
            data.insert(0, x)
            count+=1
    end = count
    if end==0 or end==1: sortStr(data, end)
    for index in range(end):
        for index2 in range(index, end):
            compare(data, data[index], data[index2], 'int')
    sortStr(data, end)


def sortAlnum(data, start, lenght):
    end = start+lenght
    for index in range(end):
        for index2 in range(index, end):
            compare(data, data[index], data[index2], 'alnum', start, end)

    return data, start+lenght


def sortStr(data, start):
    count = 0
    count2 = 0
    for i in range(len(data)):
        if isinstance(data[i], str):
            x = data[i]
            data.remove(data[i])
            data.insert(start, x)
            count+=1
            if isinstance(data[i][0], int):
                count2 += 1
                start+=1
    start -= count2
    data, start = sortAlnum(data, start, count2)
    end = start + count - count2
    if end-start==0 or end-start==1: return data, end
    for index in range(start, end):
        for index2 in range(index, end):
            compare(data, data[index], data[index2], 'str')
            print(data)
    return data, end

    
order = ['Enter list here to test...']
print(sortNum(order))
