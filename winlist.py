import windictionary
import datetime
import matplotlib.pyplot as plt
import numpy as np

def doublon(list, n):
    list2 = []
    for k in range(len(list)):
        if not list[k][n] in list2:
            list2.append(list[k][n])
    list2.sort()
    return list2


def word_convert(list):
    output_list=[]
    for k in range(len(list)):
        output_list.append(windictionary.vocab(list[k]))
    return output_list


def data(list1, list2):
    output = []
    for k in range(len(list1)):
        if list2[4][0] <= list1[k][6].date() <= list2[4][1]:
            if list1[k][2] == list2[1]:
                if list1[k][0] in list2[0]:
                    if list1[k][4] in list2[2]:
                        if list1[k][3] in list2[3]:
                            output.append(list1[k])
    return output

def graph(list,periode,ttype):
    x = np.linspace(1,len(list),len(list))
    y=[]
    for k in range(len(list)):
        y.append(list[k][1])
    plt.title(word_convert([ttype])[0] + ' du ' + periode[0].strftime('%d/%m/%Y') + ' au ' + periode[1].strftime('%d/%m/%Y'))
    plt.ylabel('Position')
    plt.plot(x,y)
    plt.show()