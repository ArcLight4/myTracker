import windictionary

def doublon(list,n):
    list2=[]
    for k in range(len(list)) :
        if not list[k][n] in list2 :
            list2.append(list[k][n])
    for k in range(len(list2)):
        list2[k]=windictionary.vocab(list2[k])
    list2.sort()
    return list2
