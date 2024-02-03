def unique(somelist):
    uniquelist = []
    uniquelist.append(somelist[0])
    for i in range(1, len(somelist)):
        for j in range(0, len(uniquelist)):
            if somelist[i] == uniquelist[j]:
                break 
            if j + 1 == len(uniquelist):
                uniquelist.append(somelist[i])
    print(uniquelist)

unique([1, 3, 1, 1, 2, 2, 1, 3, 3])