
def doublon(list,n):
    list2=[]
    for k in range(len(list)) :
        if not list[k][n] in list2 :
            list2.append(list[k][n])
    return list2